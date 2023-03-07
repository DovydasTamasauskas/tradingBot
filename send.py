import imaplib
from email.message import Message
from time import time


def sendMessage(connection, title, message):
    new_message = Message()
    new_message["From"] = "tradingBot@bot.com"
    new_message["Subject"] = title
    new_message.set_payload(message)

    connection.append('INBOX', '', imaplib.Time2Internaldate(
        time()), str(new_message).encode('utf-8'))
