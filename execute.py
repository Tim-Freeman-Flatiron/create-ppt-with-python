# the email creation and sending portion of this code was inspired by http://naelshiab.com/tutorial-send-email-python/
# the ppt portion of this code was inspired by https://www.youtube.com/watch?v=ia9wXLq34us

from google_api_adapter import get_spreadsheet_data_from_googlesheets
from execute_PPTs import make_all_ppts
from execute_email import create_and_send_email
import sys

def main():
  spreadsheet_data = get_spreadsheet_data_from_googlesheets()
  make_all_ppts(spreadsheet_data)
  create_and_send_email(spreadsheet_data)
  print('Done.')

if __name__ == '__main__':
	main()