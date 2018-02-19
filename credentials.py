import os

from oauth2client import client, tools
from oauth2client.file import Storage

from argparse import ArgumentParser

# If modifying SECRET_JSON, APP_NAME, or SCOPES, delete previously saved credentials
from secrets import SECRET_JSON, APP_NAME, SCOPES, CREDENTIAL_PATH

# this code has been modified from https://developers.google.com/sheets/api/quickstart/python
def get_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    
    cred_path = os.path.join(credential_dir, CREDENTIAL_PATH)
    store = Storage(cred_path)
    credentials = store.get()
    
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(SECRET_JSON, SCOPES)
        flow.user_agent = APP_NAME
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
        credentials = tools.run_flow(flow, store, flags)
        print('Storing credentials to ' + cred_path)
    
    return credentials