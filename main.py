import imaplib
import email
import time
import credentials
import json
import ib


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


POSITION = "position"
PAIR = "US30USD"
TIME = "15min"
STOP_LOSS_CANDLES = "3"
MAX_STOP_LOSS = "0.02"
TAKE_PROFIT_RATIO = "1.5"

# subject = 'BOT{"'+POSITION+'": "long","'+PAIR+'": "US30USD", "'+TIME+'": "15min", "' + \
#     STOP_LOSS_CANDLES+'": "3", "'+MAX_STOP_LOSS + \
#     '": "0.02", "'+TAKE_PROFIT_RATIO+'": "1.5"}'

while True == True:
    connection = imaplib.IMAP4_SSL(credentials.IMAP_SERVER)
    connection.login(credentials.EMAIL_ADDRESS, credentials.EMAIL_PASSWORD)
    connection.select("Inbox")
    msgs = searchUnseenMessages(connection)

    for msg in msgs[0].split():
        subject = fetchMessage(connection, msg)

        if isBotMessage(subject):
            person_dict = toJson(subject)
            print("found 1 message")
            ib.main(connection)

    sleep(5)
    connection.close()
