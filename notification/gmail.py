import imaplib
import email
from email.message import Message
import shared.log as log
import shared.consts as consts
from time import time
import credentials
import shared.functions as functions

connection = None


def sendMail(title, message):
    try:
        global connection
        connection = openConnection()
        new_message = Message()
        new_message["From"] = credentials.BOT_EMAIL_ADDRESS
        new_message["Subject"] = title
        new_message.set_payload(message)
        connection.append('INBOX', '', imaplib.Time2Internaldate(
            time()), str(new_message).encode('utf-8'))
    except:
        log.warrning(consts.FAILED_TO_SEND_EMAIL)


def searchUnseenMessages():
    try:
        global connection
        connection = openConnection()
        _, msgs = connection.search(None, "(UNSEEN)")
        messages = []
        if msgs != None:
            for msg in msgs[0].split():
                _, data = connection.fetch(msg, "(RFC822)")
                message = email.message_from_bytes(data[0][1])
                # {consts.TITLE: message.get("Subject"), consts.BODY: message.get_payload(decode=True).decode()}
                subject = message.get_payload(
                    decode=True).decode()  # get email body
                if functions.isResultMessage(subject) == False:
                    subjectJSON = functions.toJson(subject)
                    if subjectJSON != None and functions.isRequiredParamsDefined(subjectJSON):
                        messages.append(subjectJSON)
        return messages
    except:
        log.warrning(consts.FAILED_TO_SEARCH_FOR_UNSEEN_MESSAGES)
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
