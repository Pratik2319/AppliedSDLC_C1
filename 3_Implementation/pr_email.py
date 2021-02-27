import os
import smtplib
import imghdr
from email.message import EmailMessage

ADDRESS = os.environ.get('EMAIL_USER')
PASSWORD = os.environ.get('EMAIL_PASS')

