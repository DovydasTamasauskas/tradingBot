import imaplib
import email
import time
import credentials
import json
import ib
import sys


def sleep(sleepTime):
    for x in range(sleepTime):
        time.sleep(1)
        print(sleepTime-x, end="\r")


def slice(val, start=0, end=None):
    return val[start:end]


def toJson(subject):
    return json.loads(slice(subject, 3))


def searchUnseenMessages(connection):
    _, msgs = connection.search(None, "(UNSEEN)")
    return msgs


def fetchMessage(connection, msg):
    _, data = connection.fetch(msg, "(RFC822)")
    message = email.message_from_bytes(data[0][1])
    subject = message.get("Subject")
    return subject


def isBotMessage(subject):
    return subject[0:3] == "BOT"


def handleNewMessage(connection, subject):
    if len(subject) > 10:
        params = toJson(subject)
        print("found 1 message")
        ib.main(connection, params)
    else:
        print("message its too short")


def isTest():
    arg = sys.argv
    if len(arg) > 1:
        return sys.argv[1] == 'test'
    return False


def open_connection():
    connection = imaplib.IMAP4_SSL(credentials.IMAP_SERVER)
    connection.login(credentials.EMAIL_ADDRESS,
                     credentials.EMAIL_PASSWORD)
    connection.select("Inbox")
    return connection


def main():
    if isTest() == False:
        while True == True:
            connection = open_connection()
            msgs = searchUnseenMessages(connection)

            for msg in msgs[0].split():
                subject = fetchMessage(connection, msg)

                if isBotMessage(subject):
                    handleNewMessage(connection, subject)

            sleep(5)
            connection.close()
    else:
        connection = open_connection()
        subject = 'BOT{"position": "long", "pair": "EURUSD", "time": "15 mins", "stopLossCanldes": "2", "maxStopLoss": "0.02", "takeProfitRatio": "1.5"}'
        handleNewMessage(connection, subject)


main()
