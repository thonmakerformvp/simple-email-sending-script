import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

ROOT_EMAIL = "YOUR_EMAIL"
ROOT_PASSWORD = "YOUR_EMAIL_PASSWORD"

people_to_email = ["EMAIL OF PERSON TO EMAIL1", "EMAIL OF PERSON TO EMAIL2"]
for person in people_to_email:
	subject = "This is the email subject"

	MESSAGE = MIMEMultipart('alternative')
	MESSAGE['subject'] = subject
	MESSAGE['To'] = person
	MESSAGE['From'] = ROOT_EMAIL
	MESSAGE.preamble = "Sorry your email is not supported"

	parameter_to_email1 = "Dave"
	email_content = "Hi there %s! " % (parameter_to_email1)
	

	HTML_BODY = MIMEText(email_content, 'html')
	MESSAGE.attach(HTML_BODY)

	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()

	server.login(ROOT_EMAIL, ROOT_PASSWORD)
	server.sendmail(ROOT_EMAIL, person, MESSAGE.as_string())
	server.quit()

	print 'successfully sent the mail'
