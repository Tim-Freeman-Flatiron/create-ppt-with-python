from google_api_adapter import connect_to_googlesheets, extract_spreadsheet_tabs
from secrets import DATASET_SHEET_ID
import datetime

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
    if 'PW' in column and not 'Change' in column:
      previous_pw_column = index
    if 'GPA' in column and not 'Change' in column:
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
  
  date = str(datetime.date.today().month) + '/' + str(datetime.date.today().day)
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

def sort_students_by_data(students_list, attribute, descending, number_of_students_to_return):
  student_ids = list(students_list.keys())
  sortable_data = []
  for stu_id in student_ids:
    temp_obj = students_list[stu_id]
    temp_obj['id'] = stu_id
    sortable_data.append(temp_obj)
  print(sorted(sortable_data, key=lambda student: student[attribute], reverse=descending)[0:number_of_students_to_return])

def main():
  api = connect_to_googlesheets()
  tabs = extract_spreadsheet_tabs(api, DATASET_SHEET_ID)
  current_data = extract_relevant_data(api, DATASET_SHEET_ID, tabs, 'CurrentData', '!A1:AE')
  current_students = make_current_students(current_data)
  master_data = extract_relevant_data(api, DATASET_SHEET_ID, tabs, 'Q3 Master', '!1:250')
  final_data = add_current_data_to_master(master_data, current_students)
  # write_new_master_to_sheet(api, DATASET_SHEET_ID, 'Q3 Master', final_data['master_data'])
  pw_jumpers = sort_students_by_data(final_data['current_students'], 'pw_change', False, 5)
  pw_leaders = sort_students_by_data(final_data['current_students'], 'pw_avg', False, 5)
  gpa_jumpers = sort_students_by_data(final_data['current_students'], 'gpa_change', False, 5)



if __name__ == '__main__':
  main()