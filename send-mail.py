from smtplib import SMTP

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from string import Template

FROM_EMAIL = '<from_email>'
FROM_EMAIL_PASSWORD = '********'

RECEIVER_NAME = '<recipient_name>'
RECEIVER_EMAIL = '<recipient_email>'


def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


server = SMTP(host='smtp.gmail.com', port=587)
server.starttls()
server.login(FROM_EMAIL, FROM_EMAIL_PASSWORD)

message_template = read_template('template_reboot.txt')

msg = MIMEMultipart()
msg['From'] = FROM_EMAIL
msg['To'] = RECEIVER_EMAIL
msg['Subject'] = '[Ping] A Reboot happened'

message = message_template.substitute(RECIPIENT_NAME=RECEIVER_NAME)
print(message)

msg.attach(MIMEText(message, 'plain'))

server.send_message(msg)
del msg

server.quit()

print('Complete! Mail sent successfully.')
