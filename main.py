import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP_SSL('smtp.example.com', 465)

server.ehlo()

with open('password.txt', 'r') as f:
    password = f.read()

server.login('thatsme@example.com', password)

msg = MIMEMultipart()
msg['From'] = 'thatsme@example.com'
msg['To'] = 'testing@spaml.de'
msg['Subject'] = 'Just a Test'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'coding.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('thatsme@example.com', 'testing@spaml.de', text)
