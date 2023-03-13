import imaplib
import email
from email.message import Message
from time import time
import credentials


def sendMessage(connection, title, message):
    new_message = Message()
    new_message["From"] = "tradingBot@bot.com"
    new_message["Subject"] = title
    new_message.set_payload(message)

    connection.append('INBOX', '', imaplib.Time2Internaldate(
        time()), str(new_message).encode('utf-8'))


def searchUnseenMessages(connection):
    _, msgs = connection.search(None, "(UNSEEN)")
    return msgs


def fetchMessage(connection, msg):
    _, data = connection.fetch(msg, "(RFC822)")
    message = email.message_from_bytes(data[0][1])
    subject = message.get("Subject")
    return subject


def openConnection():
    connection = imaplib.IMAP4_SSL(credentials.IMAP_SERVER)
    connection.login(credentials.EMAIL_ADDRESS,
                     credentials.EMAIL_PASSWORD)
    connection.select("Inbox")
    return connection
