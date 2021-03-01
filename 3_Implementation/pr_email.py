"""This fie is for sending automated emails"""
import os
import smtplib
import imghdr
from email.message import EmailMessage


def send_email(d2):
    """To send the email"""
    try:
        ADDRESS = "fortestinginpython@gmail.com"
        PASSWORD = "Sdlc#2021"    #should be encrypted
        d1 = d2
        d1['faculty'] = "prithvi.pagala@ltts.com"
        
        for value in d1.items():
            msg = EmailMessage()
            msg['Subject'] = f"TEST/SURVEY RESULTS for {value[0]}"
            msg['From'] = ADDRESS
            msg['To'] = value[1]         
            msg.set_content('Please find your Results')

            path = f"C:/Users/mithu/AppliedSDLC_C1/3_Implementation/{str(d1[0])}"

            for i in os.walk(path):      
                plots = i[2]                                                     

            for plot in plots:
                with open(plot, 'rb') as f:
                    file_data = f.read()
                    file_type = imghdr.what(f.name)
                    file_name = f.name
                    
                msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(ADDRESS, PASSWORD)
                smtp.send_message(msg)
    except:
        print("Add files to send the mail")
