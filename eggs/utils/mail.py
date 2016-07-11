# -*- coding: utf-8 -*-
import email
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

USER = 'ops@chinascopefinancial.com'
PASSWORD = 'GmgW3UXF'
HOST = 'mail.chinascopefinancial.com'
PORT = 0


class Sender(object):
    def __init__(self, user=None, password=None, host=None, port=25,
                 receivers=None, subtype='mixed', timeout=60):
        self.user = user or USER
        self.password = password or PASSWORD
        self.host = host or HOST
        self.port = PORT
        self.timeout = timeout
        self.receivers = receivers or []

        self.msg = MIMEMultipart(subtype)

    def connect(self):
        self.smtp = smtplib.SMTP(timeout=self.timeout)
        self.smtp.connect(self.host, self.port)
        self.smtp.login(self.user, self.password)

    def add_header(self, subject, priority=1):
        self.msg['From'] = Header(self.user)
        self.msg['To'] = Header(';'.join(self.receivers), 'utf-8')
        self.msg["Date"] = email.utils.formatdate(localtime=True)
        self.msg['Subject'] = Header('Subject: ' + subject, 'utf-8')
        self.msg['X-Priorit'] = Header(str(priority), 'utf-8')

    def send_email(self, subject, body, attaches=None):
        self.add_header(subject)
        smtp = smtplib.SMTP(timeout=self.timeout)
        smtp.connect(self.host, self.port)
        smtp.login(self.user, self.password)

        for attach in attaches or []:
            att = MIMEText(attach['attach_text'], 'base64', 'utf-8')
            att["Content-Type"] = 'application/octet-stream'
            att["Content-Disposition"] = 'attachment; filename="%s"' % attach['attach_name']
            self.msg.attach(att)

        self.msg.attach(MIMEText(body, 'plain', 'utf-8'))
        smtp.sendmail(self.user, self.receivers, self.msg.as_string())
        smtp.quit()
