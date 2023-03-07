import imaplib
import email
import time
import credentials
import json
import send


def sleep(sleepTime):
    for x in range(sleepTime):
        time.sleep(1)
        print(sleepTime-x, end="\r")


imap_server = credentials.IMAP_SERVER
email_address = credentials.EMAIL_ADDRESS
password = credentials.EMAIL_PASSWORD


def slice(val, start=0, end=None):
    return val[start:end]


def toJson(subject):
    return json.loads(slice(subject, 3))


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
    imap = imaplib.IMAP4_SSL(imap_server)
    imap.login(email_address, password)
    imap.select("Inbox")
    _, msgs = imap.search(None, "(UNSEEN)")
    print("getting messages")

    for msg in msgs[0].split():
        _, data = imap.fetch(msg, "(RFC822)")
        message = email.message_from_bytes(data[0][1])
        subject = message.get("Subject")
        print(subject)

        if subject[0:3] == "BOT":
            person_dict = toJson(subject)
            print(person_dict[POSITION])
            send.sendMessage(imap, "tihis is a title", "main")
    sleep(5)
    imap.close()
