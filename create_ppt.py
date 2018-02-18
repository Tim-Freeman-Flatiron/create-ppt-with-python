import os

from apiclient import discovery
import httplib2

from pptx import Presentation
from pptx.util import Inches

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64

from credentials import get_credentials

from secrets import FROM_EMAIL, FROM_PASSWORD, TO_EMAIL, SHEET_ID

def convert_file_to_attachment(file):
	file_name = file.split('/')[-1]
	file_object = open(file, 'rb')
	attachment = MIMEBase('application', 'octet-stream')
	attachment.set_payload((file_object).read())
	encode_base64(attachment)
	attachment.add_header('Content-Disposition', "attachment; filename= %s" % file_name)
	return attachment

def send_email_with_attachments(files_to_attach):
	message = MIMEMultipart()
	message['From'] = FROM_EMAIL
	message['To'] = TO_EMAIL
	message['Subject'] = 'This Week\'s Community Meeting Powerpoints'

	for file in files_to_attach:
		attachment = convert_file_to_attachment(file)
		message.attach(attachment)

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(FROM_EMAIL, FROM_PASSWORD)
	text = message.as_string()
	server.sendmail(FROM_EMAIL, TO_EMAIL, text)
	server.quit()

def proccess_tabs(tabs, service, spreadsheetId):
	parsed_tabs = []

	for tab in tabs:
		tab_name = tab.get('properties', {}).get('title')
		rangeName = tab_name + '!A2:C'
		result = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=rangeName).execute()
		student_data = result.get('values', [])
		file_path = make_path(tab_name)
		tab_object = {'file': file_path, 'student_data': student_data}
		parsed_tabs.append(tab_object)

	return parsed_tabs

def make_path(tab_name):
	return os.getcwd() + '/' + tab_name + '.pptx'

def make_all_ppts(parsed_tabs):
	for tab in parsed_tabs:
		file_path = tab['file']
		student_data = tab['student_data']
		make_ppt(file_path, student_data)

def make_ppt(file_path, student_data):
	presentation = Presentation()
	blank_slide_layout = presentation.slide_layouts[6]
	slide = presentation.slides.add_slide(blank_slide_layout)

	r = 0
	placeholder = 0
	left = 0.5
	top = 1
	width = 1
	height = 1

	for row in student_data:
		if r > 0:
			if placeholder == 34:
				slide = presentation.slides.add_slide(blank_slide_layout)
				placeholder = 0
				left = 0.5
				top = 1
			if placeholder == 12 or placeholder == 24:
				left = left + 3
				top = 1
			first_name = row[0]
			last_name = row[1]
			pwa = row[2]
			textBox = slide.shapes.add_textbox(Inches(left),Inches(top),Inches(width),Inches(height))
			textBox.text_frame.text = first_name + ' ' + last_name + ' ' + pwa
			placeholder = placeholder+1
			top = top+0.5
		r = r+1

	presentation.save(file_path)

def isolate_file_names_for_attachments(parsed_tabs):
	file_names = []
	
	for tab in parsed_tabs:
		file_names.append(tab['file'])

	return file_names

def main():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?''version=v4')
    service = discovery.build('sheets', 'v4', http=http, discoveryServiceUrl=discoveryUrl)  
    tabs = service.spreadsheets().get(spreadsheetId=SHEET_ID).execute().get('sheets', '')
    processed_tabs = proccess_tabs(tabs, service, SHEET_ID)
    make_all_ppts(processed_tabs)
    files = isolate_file_names_for_attachments(processed_tabs)
    send_email_with_attachments(files)


if __name__ == '__main__':
    main()