from google_api_adapter import connect_to_googlesheets, extract_spreadsheet_tabs
from secrets import DATASET_SHEET_ID
import datetime
from os import getcwd as get_current_directory
from pptx import Presentation
from pptx.util import Inches
from execute_email import create_and_send_email
from CommunityMeeting import CommunityMeeting
import logging
logging.basicConfig(filename='debug.log',level=logging.DEBUG)

def extract_relevant_data(api, DATASET_SHEET_ID, tabs, relevant_tab_name, data_range):
  for tab in tabs:
    tab_name = tab.get('properties', {}).get('title')
    if tab_name == relevant_tab_name:
      data_range = tab_name + data_range
      data = api.spreadsheets().values().get(spreadsheetId=DATASET_SHEET_ID, range=data_range).execute()
  data = data.get('values', [])
  return data

def make_current_students(current_data):
  headers = current_data[0]
  for index, column in enumerate(headers):
    if column == 'Student Id':
      student_id = index
    elif column == 'HW Avg':
      current_pw_avg = index
    elif column == 'Weighted Live GPA':
      current_gpa = index

  student_data = {}
  r = 0
  for student in current_data:
    if r > 0:
      key = student[student_id]
      value = {'pw_avg': student[current_pw_avg], 'gpa': student[current_gpa]}
      student_data[key] = value
    r += 1
  return student_data

def add_current_data_to_master(master_data, current_students):
  headers = master_data[0]
# find right columns
  for index, column in enumerate(headers):
    if column == 'HS Dashboard ID':
      id_column = index
    if 'PW' in column and 'Change' not in column:
      previous_pw_column = index
    if 'GPA' in column and 'Change' not in column:
      previous_gpa_column = index
    if column == 'last_name':
      last_name = index
    if column == 'first_name':
      first_name = index
  r = 0
  for master_student in master_data:
    if r > 0:
      student_id = master_student[id_column]
      student_last_name = master_student[last_name]
      student_first_name = master_student[first_name]
      current_student = current_students.get(student_id, {})

      current_pw_avg = current_student.get('pw_avg').replace('%', '')
      current_gpa = current_student.get('gpa')

      master_student.append(current_pw_avg)
      master_student.append(current_gpa)

      previous_pw = master_student[previous_pw_column]
      previous_gpa = master_student[previous_gpa_column]

      pw_change = ''
      if previous_pw and current_pw_avg:
        pw_change = int(current_pw_avg) - int(previous_pw)

      gpa_change = ''
      if previous_gpa and current_gpa:
        gpa_change = round((float(current_gpa) - float(previous_gpa)), 2)

      master_student.append(pw_change)
      master_student.append(gpa_change)
      current_student['first_name'] = student_first_name
      current_student['last_name'] = student_last_name
      current_student['pw_change'] = pw_change
      current_student['gpa_change'] = gpa_change
    r += 1
  today = str(datetime.date.today().day)
  month = str(datetime.date.today().month)
  date = month + '/' + today
  new_headers = ['PW', 'GPA', 'PW Change', 'GPA Change']
  for header in new_headers:
    line = '{} {}'.format(date, header)
    master_data[0].append(line)

  final_data = {}
  final_data['master_data'] = master_data
  final_data['current_students'] = current_students
  return final_data

def write_new_master_to_sheet(api, DATASET_SHEET_ID, master_tab_name, final_data):
  range_max = len(final_data)
  range_name = '{}!1:{}'.format(master_tab_name,range_max)
  body = {'values': final_data}
  api.spreadsheets().values().update(spreadsheetId=DATASET_SHEET_ID, range=range_name,valueInputOption='RAW',body=body).execute()

def separate_students_by_data_group(students_list, attribute):
  student_ids = list(students_list.keys())
  separated_students = []
  for stu_id in student_ids:
    student = students_list[stu_id]
    temp_obj = {}
    temp_obj['id'] = stu_id
    temp_obj['first_name'] = student['first_name']
    temp_obj['last_name'] = student['last_name']
    temp_obj['data'] = student[attribute]
    separated_students.append(temp_obj)

    # separated_students = sorted(sortable_data, key=lambda student: student['data'], reverse=True)
  for student in separated_students:
    if 'change' in attribute:
      student['data'] = '+' + str(student['data'])
    else:
      student['data'] = str(student['data'])
  return separated_students

def main():
  api = connect_to_googlesheets()
  tabs = extract_spreadsheet_tabs(api, DATASET_SHEET_ID)
  current_data = extract_relevant_data(api, DATASET_SHEET_ID, tabs, 'CurrentData', '!A1:AE')
  current_students = make_current_students(current_data)
  master_data = extract_relevant_data(api, DATASET_SHEET_ID, tabs, 'Q4 Master', '!1:250')
  today = str(datetime.date.today().month) + '/' + str(datetime.date.today().day)
  written_to_master = True if today in ' '.join(master_data[0]) else False
  final_data = add_current_data_to_master(master_data, current_students)

  if not written_to_master:
    write_new_master_to_sheet(api, DATASET_SHEET_ID, 'Q4 Master', final_data['master_data'])

  unsorted_pw_jumpers = list(filter((lambda student: int(student['data'][1:]) > 0),separate_students_by_data_group(final_data['current_students'], 'pw_change')))
  sorted_pw_jumpers = sorted(unsorted_pw_jumpers, key=lambda student: int(student['data'][1:]))

  if len(sorted_pw_jumpers) > 108:
    start = len(sorted_pw_jumpers) - 108
    sorted_pw_jumpers = sorted_pw_jumpers[start:]

  for student in sorted_pw_jumpers:
    student['data'] = student['data'] + '%'

  unsorted_pw_leaders = list(filter((lambda student: int(student['data'][:-1]) >= 85),separate_students_by_data_group(final_data['current_students'], 'pw_avg')))
  sorted_pw_leaders = sorted(unsorted_pw_leaders, key=lambda student: int(student['data'][:-1]))

  unsorted_gpa_jumpers = list(filter((lambda student: float(student['data'][1:]) > 0.0),separate_students_by_data_group(final_data['current_students'], 'gpa_change')))
  sorted_gpa_jumpers = sorted(unsorted_gpa_jumpers, key=lambda student: float(student['data'][1:]))

  if len(sorted_gpa_jumpers) > 108:
    start = len(sorted_gpa_jumpers) - 108
    sorted_gpa_jumpers = sorted_gpa_jumpers[start:]

  date = str(datetime.date.today().month).rjust(2, '0') + '_' + str(datetime.date.today().day) + '_' + str(datetime.date.today().year)[2:]

  pwjumpers_path = '{}/PowerPoints/{}_PWJumpers.pptx'.format(get_current_directory(),date)
  pwleaders_path = '{}/PowerPoints/{}_PWLeaders.pptx'.format(get_current_directory(),date)
  gpajumpers_path = '{}/PowerPoints/{}_GPAJumpers.pptx'.format(get_current_directory(),date)

  comm_meeting = CommunityMeeting()
  comm_meeting.make_ppt(pwjumpers_path, sorted_pw_jumpers)
  comm_meeting.make_ppt(pwleaders_path, sorted_pw_leaders)
  comm_meeting.make_ppt(gpajumpers_path, sorted_gpa_jumpers)

  create_and_send_email([pwjumpers_path, pwleaders_path, gpajumpers_path])

if __name__ == '__main__':
  main()
