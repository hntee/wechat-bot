import smtplib
import threading
import os

from email.mime.multipart import MIMEMultipart
from email.message import Message
from email.header import Header

EMAIL_FROM = os.environ['EMAIL_FROM']
EMAIL_TO = os.environ['EMAIL_TO']
EMAIL_PASSWORD = os.environ['EMAIL_PASSWORD']

class SendEmailThread(threading.Thread):
    """send html email"""
    def __init__(self, subject, to=EMAIL_TO):
        self.to = to
        self.msg = Message()
        self.msg['Subject'] = subject
        self.msg['From'] = EMAIL_FROM
        self.msg['To'] = to
        threading.Thread.__init__(self)

    def run(self):
        self.send()

    def send(self):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(EMAIL_FROM, EMAIL_PASSWORD)
        server.sendmail(EMAIL_FROM, self.to, self.msg.as_string())

def sendmail(subject):
    send_email_thread = SendEmailThread(subject)
    send_email_thread.start()

