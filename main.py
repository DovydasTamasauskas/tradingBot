import time
import json
import handlers.positionHandler as positionHandler
import sys
import notification.notify as notification
import shared.functions as functions
import shared.consts as consts


def sleep(sleepTime):
    for x in range(sleepTime):
        time.sleep(1)
        print(sleepTime-x, end="\r")


def toJson(subject):
    try:
        return json.loads(functions.slice(subject, 3))
    except:
        print(consts.FAILED_TO_READ_PROPS)
        sys.exit()


def isBotMessage(subject):
    prefix = consts.BOT
    return subject[0:len(prefix)] == prefix


def handleNewMessage(connection, subject):
    if len(subject) > len(consts.BOT):
        params = toJson(subject)
        print(consts.MESSAGE_FOUND)
        positionHandler.handlePosition(connection, params)
    else:
        print(consts.FAILED_TO_READ_PROPS)


def isTest():
    arg = sys.argv
    if len(arg) > 1:
        return sys.argv[1] == consts.TEST
    return False


def main():
    if isTest() == False:
        while True == True:
            connection = notification.openConnection()
            msgs = notification.searchUnseenMessages(connection)

            for msg in msgs[0].split():
                subject = notification.fetchMessage(connection, msg)

                if isBotMessage(subject):
                    handleNewMessage(connection, subject)

            sleep(5)
            connection.close()
    else:
        connection = notification.openConnection()
        print(consts.TEST_RUNNING_MESSAGE)
        positionHandler.handlePosition(connection, consts.TEST_JSON)


if __name__ == "__main__":
    main()
