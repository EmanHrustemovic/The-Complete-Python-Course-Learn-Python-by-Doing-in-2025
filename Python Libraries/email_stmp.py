import smtplib
from email.message import EmailMessage

email = EmailMessage()

email_content = ''' Dear Sir/Madam,

I am sending you e-mail via Python. I hope you like it.

Kind regards,
Eman

'''

email['Subject'] = 'Test email.'
email['From'] = 'you@gmail.com'
email['To'] = 'someone@gmail.com'

email.set_content(email_content)

smtp_connector = smtplib.SMTP(host='smtp.gmail.com', port=587) #587 is port for GMAIL
smtp_connector.starttls()
smtp_connector.login('you@gmail.com','password')

smtp_connector.send_message(email)