

from flask_mail import Message
from ..extensions import mail

def sendMail1(message1):
    mail.send(message1)