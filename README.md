# python_mail_client
simple mail client to work with public mail services

## Usage
- create password.txt file with your mail account password (**encrypt if you're doing it on public computer!**)
- message(body) is in separate file `message.txt` for convenience
- any attachments should be attached like this (e.g. you want to attach image from `coding.jpg` file):
```python
filename = 'coding.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)
```
- read docs for email module to change anything you like
