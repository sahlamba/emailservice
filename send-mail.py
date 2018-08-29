#!/usr/bin/python3
import os
import codecs

from smtplib import SMTP

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from string import Template

from dotenv import load_dotenv
load_dotenv()

dir_path = os.path.dirname(os.path.abspath(__file__))

FROM_EMAIL = os.getenv('SENDER_EMAIL')
FROM_EMAIL_PASSWORD = os.getenv('SENDER_EMAIL_PASSWORD')

RECEIVER_NAME = 'Sahil'
RECEIVER_EMAIL = 'sahil.lamba95@gmail.com'


def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


server = SMTP(host='smtp.gmail.com', port=587)
server.starttls()
server.login(FROM_EMAIL, FROM_EMAIL_PASSWORD)

plain_message_template = read_template(os.path.join(dir_path, 'template_plain_reboot.txt'))
html_message_template = codecs.open(os.path.join(dir_path, 'template_html_reboot.html'), 'r').read()

msg = MIMEMultipart('alternative')
msg['From'] = FROM_EMAIL
msg['To'] = RECEIVER_EMAIL
msg['Subject'] = '[Ping] A Boot/Reboot happened'

plain_message = plain_message_template.substitute(RECIPIENT_NAME=RECEIVER_NAME)
print(plain_message)

html_message = html_message_template.format(RECIPIENT_NAME=RECEIVER_NAME)
print(html_message)

msg.attach(MIMEText(plain_message, 'plain'))
msg.attach(MIMEText(html_message, 'html'))

server.send_message(msg)
del msg

server.quit()

print('Complete! Mail sent successfully.')
