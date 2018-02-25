# for google api calls
from apiclient import discovery as api
from httplib2 import Http
from os import getcwd as get_current_directory
from credentials import get_credentials # relative import of function to verify credentials
from secrets import SHEET_ID

def get_spreadsheet_data_from_googlesheets():
  googlesheets = connect_to_googlesheets()
  tab_names = extract_spreadsheet_tabs(googlesheets, SHEET_ID)
  tab_objects = process_data(tab_names, googlesheets)
  return tab_objects

def connect_to_googlesheets():
  print('Connecting to GoogleSheets...')
  api_credentials = get_credentials()
  http = api_credentials.authorize(Http())
  api_url = ('https://sheets.googleapis.com/$discovery/rest?''version=v4')
  googlesheets = api.build('sheets', 'v4', http=http, discoveryServiceUrl=api_url)
  print('- Successfully established connection to GoogleSheets.')
  return googlesheets

def extract_spreadsheet_tabs(googlesheets, SHEET_ID):
  print('Extracting individual tabs from the spreadsheet...')
  tab_names = googlesheets.spreadsheets().get(spreadsheetId=SHEET_ID).execute().get('sheets', '')
  print('- Tab extraction successful.')
  return tab_names

def process_data(tab_names, googlesheets):
  tab_objects = []
  for tab in tab_names:
    tab_name = tab.get('properties', {}).get('title')
    print('- Processing {}...'.format(tab_name))
    range_name = tab_name + '!A2:C'
    tab_data = googlesheets.spreadsheets().values().get(spreadsheetId=SHEET_ID, range=range_name).execute()
    student_data = tab_data.get('values', [])
    file_path = get_current_directory() + '/PowerPoints/' + tab_name + '.pptx'
    tab_object = {
                  'file': file_path,
                  'student_data': student_data
                  }
    tab_objects.append(tab_object)
  print('- Finished processing tabs.')
  return tab_objects