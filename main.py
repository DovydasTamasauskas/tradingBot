import json
import test
import handlers.positionHandler as positionHandler
import notification.notify as notification
import shared.functions as functions
import shared.print as print
import shared.consts as consts

SLEEP_INTERVAL_SEC = 5


def isBotMessage(subject):
    prefix = consts.BOT
    return subject[0:len(prefix)] == prefix


def handleNewMessage(connection, subject):
    if len(subject) > len(consts.BOT):
        params = functions.toJson(subject)
        print.info(consts.MESSAGE_FOUND)
        positionHandler.handlePosition(connection, params)
    else:
        print.warrning(consts.FAILED_TO_READ_PROPS)


def main():
    while True == True:
        connection = notification.openConnection()
        msgs = notification.searchUnseenMessages(connection)

        for msg in msgs[0].split():
            subject = notification.fetchMessage(connection, msg)

            if isBotMessage(subject):
                handleNewMessage(connection, subject)

        functions.sleep(SLEEP_INTERVAL_SEC)
        connection.close()


if __name__ == "__main__":
    test.runTests()  # run tests form sys props - $python3 main.py test
    main()
