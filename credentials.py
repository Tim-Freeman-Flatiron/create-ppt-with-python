# this code has been modified from https://developers.google.com/sheets/api/quickstart/python 
from __future__ import print_function
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import os

from secrets import SECRET_JSON, APP_NAME, CREDENTIAL_PATH

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = SECRET_JSON
APPLICATION_NAME = APP_NAME

def get_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    cred_path = os.path.join(credential_dir, CREDENTIAL_PATH)

    store = Storage(cred_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + cred_path)
    return credentials