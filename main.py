import time
import json
import positionHandler
import sys
import notification.notify as notification
import shared.functions as functions


def sleep(sleepTime):
    for x in range(sleepTime):
        time.sleep(1)
        print(sleepTime-x, end="\r")


def toJson(subject):
    return json.loads(functions.slice(subject, 3))


def isBotMessage(subject):
    return subject[0:3] == "BOT"


def handleNewMessage(connection, subject):
    if len(subject) > 10:
        params = toJson(subject)
        print("found 1 message")
        positionHandler.handlePosition(connection, params)
    else:
        print("message its too short")


def isTest():
    arg = sys.argv
    if len(arg) > 1:
        return sys.argv[1] == 'test'
    return False


def main():
    if isTest() == False:
        while True == True:
            connection = notification.open_connection()
            msgs = notification.searchUnseenMessages(connection)

            for msg in msgs[0].split():
                subject = notification.fetchMessage(connection, msg)

                if isBotMessage(subject):
                    handleNewMessage(connection, subject)

            sleep(5)
            connection.close()
    else:
        connection = notification.open_connection()
        subject = 'BOT{"position": "long", "pair": "EURUSD", "time": "15 mins", "stopLossCanldes": 3, "maxStopLoss": 0.02, "takeProfitRatio": 1.5, "historyDataInterval": "1 D"}'
        handleNewMessage(connection, subject)


if __name__ == "__main__":
    main()
