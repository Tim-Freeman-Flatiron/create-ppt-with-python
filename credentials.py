import os

from oauth2client import client, tools
from oauth2client.file import Storage

from argparse import ArgumentParser

# If modifying SECRET_JSON, APP_NAME, or SCOPES, delete previously saved credentials
from secrets import SECRET_JSON, APP_NAME, SCOPES, CREDENTIAL_PATH, CREDENTIAL_DIRECTORY

# this code has been modified from https://developers.google.com/sheets/api/quickstart/python
def get_credentials():
    if not os.path.exists(CREDENTIAL_DIRECTORY):
        os.makedirs(CREDENTIAL_DIRECTORY)

    credential_path = os.path.join(CREDENTIAL_DIRECTORY, CREDENTIAL_PATH)
    credentials_store = Storage(credential_path)
    credentials = credentials_store.get()

    if not credentials or credentials.invalid:
        credentials_api_adapter = client.flow_from_clientsecrets(SECRET_JSON, SCOPES)
        credentials_api_adapter.user_agent = APP_NAME
        flags = ArgumentParser(parents=[tools.argparser]).parse_args()
        credentials = tools.run_flow(credentials_api_adapter, credentials_store, flags)
        print('Storing credentials to ' + credential_path)

    return credentials
