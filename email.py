import smtplib
import os
EMAIL_FROM = os.environ['EMAIL_FROM']
EMAIL_TO = os.environ['EMAIL_TO']
EMAIL_PASSWORD = os.environ['EMAIL_PASSWORD']

class Mail:
    def __init__(self):
        # self.server = smtplib.SMTP_SSL('smtp.exmail.qq.com:465')
        # self.server.login("email", "pw")
        self.server = smtplib.SMTP("smtp.gmail.com", 587)
        self.server.ehlo()
        self.server.starttls()
        self.server.ehlo()
        self.server.login(EMAIL_FROM, EMAIL_PASSWORD)

    def send(self, msg):
        message = 'Subject: {}\n'.format(msg)
        self.server.sendmail(EMAIL_FROM, EMAIL_TO, message)

