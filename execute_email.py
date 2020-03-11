from smtplib import SMTP as StartEmailServer
from email.mime.multipart import MIMEMultipart as MakeComplexEmailObject
from email.mime.text import MIMEText as MakeEmailBody
from email.mime.base import MIMEBase as MakeAttachmentObject
from email.encoders import encode_base64

from secrets import FROM_EMAIL, FROM_PASSWORD, TO_EMAIL

def create_and_send_email(attachments):
  # attachments = isolate_file_names(spreadsheet_data)
  email_with_attachments = make_email(attachments)
  send_email(email_with_attachments)

def isolate_file_names(spreadsheet_data):
  file_names = []
  for data_object in spreadsheet_data:
    file_names.append(data_object['file'])
  return file_names

def convert_file_to_attachment(file):
  file_name = file.split('/')[-1] # extract file name from absolute path
  file_object = open(file, 'rb')
  attachment = MakeAttachmentObject('application', 'octet-stream')
  attachment.set_payload(file_object.read())
  encode_base64(attachment)
  attachment.add_header('Content-Disposition', "attachment; filename= %s" % file_name)
  return attachment

def make_email(attachments):
  print('Creating email...')
  email = MakeComplexEmailObject()
  email_body = 'See attached.'
  email.attach(MakeEmailBody(email_body, 'plain'))

  email['From'] = FROM_EMAIL
  email['To'] = TO_EMAIL
  email['Subject'] = 'This Week\'s Community Meeting Powerpoints'
  print('- Attaching PowerPoints...')
  for file in attachments:
    attachment = convert_file_to_attachment(file)
    email.attach(attachment)
    print('-- Attached {}'.format(file.split('/')[-1]))

  packaged_email = email.as_string()
  print('- Email created.')
  return packaged_email

def send_email(email):
  print('Starting server...')
  server = StartEmailServer('smtp.gmail.com', 587)
  server.starttls()
  print('- Logging into Gmail...')
  server.login(FROM_EMAIL, FROM_PASSWORD)
  print('- Sending email...')
  server.sendmail(FROM_EMAIL, TO_EMAIL, email)
  server.quit()
  print('- Email sent and server ended.')
