import imaplib
import email
from email.message import Message
import shared.print as print
import shared.consts as consts
from time import time
import credentials


def sendMessage(connection, title, message):
    try:
        new_message = Message()
        new_message["From"] = credentials.BOT_EMAIL_ADDRESS
        new_message["Subject"] = title
        new_message.set_payload(message)
        connection.append('INBOX', '', imaplib.Time2Internaldate(
            time()), str(new_message).encode('utf-8'))
    except:
        print.warrning(consts.FAILED_TO_SEND_EMAIL)


def searchUnseenMessages(connection):
    try:
        _, msgs = connection.search(None, "(UNSEEN)")
    except:
        print.warrning(consts.FAILED_TO_SEARCH_FOR_UNSEEN_MESSAGES)
    return msgs


def fetchMessage(connection, msg):
    try:
        _, data = connection.fetch(msg, "(RFC822)")
        message = email.message_from_bytes(data[0][1])
        subject = message.get("Subject")
    except:
        print.warrning(consts.FAILED_TO_FETCH_MESSAGES)
    return subject


def openConnection():
    try:
        connection = imaplib.IMAP4_SSL(credentials.IMAP_SERVER)
        connection.login(credentials.EMAIL_ADDRESS,
                         credentials.EMAIL_PASSWORD)
        connection.select("Inbox")
    except:
        print.warrning(consts.FAILED_TO_OPEN_EMAIL_CONNECTION)
    return connection
