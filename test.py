
import sys
import shared.consts as consts
import shared.print as print
import notification.notify as notification
import handlers.positionHandler as positionHandler
import shared.functions as functions


TEST_JSON = {"position": "long", "pair": "EURUSD", "time": "15 mins", "time2": "15", "stopLossCanldes": 3,
             "maxStopLoss": 0.02, "takeProfitRatio": 1.5, "historyDataInterval": "1 D", "alertPrice": 1.5, "triggeredTime": "15:15:15"}


def isTest():
    arg = sys.argv
    if len(arg) > 1:
        return sys.argv[1] == consts.TEST
    return False


def runTests():
    if isTest():
        connection = notification.openConnection()
        print.info(consts.TEST_RUNNING_MESSAGE)
        positionHandler.handlePosition(connection, TEST_JSON)

        functions.sleep(5)
        # msgs = notification.searchUnseenMessages(connection)

        # for msg in msgs[0].split():
        #     subject = notification.fetchMessage(connection, msg)

        sys.exit()