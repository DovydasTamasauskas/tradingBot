
import sys
import shared.consts as consts
import notification.notify as notification
import handlers.positionHandler as positionHandler


def isTest():
    arg = sys.argv
    if len(arg) > 1:
        return sys.argv[1] == consts.TEST
    return False


def runTests():
    if isTest():
        connection = notification.openConnection()
        print(consts.TEST_RUNNING_MESSAGE)
        positionHandler.handlePosition(connection, consts.TEST_JSON)
        sys.exit()
