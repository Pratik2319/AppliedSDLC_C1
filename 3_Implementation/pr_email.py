import os
import smtplib
import imghdr
from email.message import EmailMessage

ADDRESS = os.environ.get('EMAIL_USER')
PASSWORD = os.environ.get('EMAIL_PASS')

msg = EmailMessage()
msg['Subject']
msg['From']
msg['To']
msg.set_content()

with open('random.jpg', 'r') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name
    
msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(ADDRESS, PASSWORD)
    smtp.send_message(msg)