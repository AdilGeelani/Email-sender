import smtplib
from email.message import  EmailMessage
from string import Template
from pathlib import Path # os.path like we can import html by giving path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Name'
email['to'] = 'email@gmail.com'
email['subject'] = 'subject'


email.set_content(html.substitute({'name' :'name'}), 'html')
# the substitute make $ to be replaced by the name and make it html file

with smtplib.SMTP(host ='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('fromemail@gmail.com', 'passord')
    smtp.send_message(email)
    print('all good boss')