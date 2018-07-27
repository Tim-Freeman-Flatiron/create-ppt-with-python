# for google api calls
from apiclient import discovery
from httplib2 import Http
from credentials import get_credentials # relative import of function to verify credentials

class GoogleSheets():
    def __init__(self):
        self.credentials = get_credentials()
        self.connection = self.connect_to_googlesheets()

    def connect_to_googlesheets(self):
        print('Connecting to GoogleSheets...')
        http = self.credentials.authorize(Http())
        api_url = ('https://sheets.googleapis.com/$discovery/rest?''version=v4')
        googlesheets = discovery.build('sheets', 'v4', http=http, discoveryServiceUrl=api_url)
        print('- Successfully established connection to GoogleSheets.')
        return googlesheets

    def get_tabs(self, DATASET_SHEET_ID):
        print('Extracting individual tabs from the spreadsheet...')
        tabs = self.connection.spreadsheets().get(spreadsheetId=DATASET_SHEET_ID).execute().get('sheets', '')
        print('- Tab extraction successful.')
        return tabs

    def get_relevant_data(self, DATASET_SHEET_ID, relevant_tab_name, data_range):
        tabs = self.get_tabs(DATASET_SHEET_ID)
        for tab in tabs:
            tab_name = tab.get('properties', {}).get('title')
            if tab_name == relevant_tab_name:
                data_range = tab_name + data_range
                data = self.connection.spreadsheets().values().get(spreadsheetId=DATASET_SHEET_ID, range=data_range).execute()
        data = data.get('values', [])
        return data
