import imaplib
from email.message import Message
from time import time
import credentials

connection = imaplib.IMAP4_SSL(credentials.IMAP_SERVER)
connection.login(credentials.EMAIL_ADDRESS, credentials.EMAIL_PASSWORD)


def sendMessage(connection, title, message):
    new_message = Message()
    new_message["From"] = "dovydas@bot.com"
    new_message["Subject"] = title
    new_message.set_payload(message)

    connection.append('INBOX', '', imaplib.Time2Internaldate(
        time()), str(new_message).encode('utf-8'))
