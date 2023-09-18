import imaplib
import email
from email.message import Message
import shared.log as log
import shared.consts as consts
from time import time
import credentials


def sendMail(title, message):
    try:
        connection = openConnection()
        new_message = Message()
        new_message["From"] = credentials.BOT_EMAIL_ADDRESS
        new_message["Subject"] = title
        new_message.set_payload(message)
        connection.append('INBOX', '', imaplib.Time2Internaldate(
            time()), str(new_message).encode('utf-8'))
    except:
        log.warrning(consts.FAILED_TO_SEND_EMAIL)


def searchUnseenMessages(connection):
    try:
        _, msgs = connection.search(None, "(UNSEEN)")
        return msgs
    except:
        log.warrning(consts.FAILED_TO_SEARCH_FOR_UNSEEN_MESSAGES)
    return None


def fetchMessage(connection, msg):
    try:
        _, data = connection.fetch(msg, "(RFC822)")
        message = email.message_from_bytes(data[0][1])
        return {'subject': message.get("Subject"), 'body': message.get_payload(decode=True)}
    except:
        log.warrning(consts.FAILED_TO_FETCH_MESSAGES)
    return None


def openConnection():
    try:
        connection = imaplib.IMAP4_SSL(credentials.IMAP_SERVER)
        connection.login(credentials.EMAIL_ADDRESS,
                         credentials.EMAIL_PASSWORD)
        connection.select("Inbox")
        return connection
    except:
        log.warrning(consts.FAILED_TO_OPEN_EMAIL_CONNECTION)
    return None
