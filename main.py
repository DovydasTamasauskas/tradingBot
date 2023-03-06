import imaplib
import email
import time
import credentials


def sleep(sleepTime):
    for x in range(sleepTime):
        time.sleep(1)
        print(sleepTime-x, end="\r")


imap_server = credentials.IMAP_SERVER
email_address = credentials.EMAIL_ADDRESS
password = credentials.EMAIL_PASSWORD

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
        splited = subject.split()
        print(splited)
        requirements = ["stopLoss", "maxStopLoss"]
        if splited[0].find(requirements[0]):
            if splited[0].find("="):
                print(splited[0].split("=")[1])
    sleep(5)
    imap.close()
