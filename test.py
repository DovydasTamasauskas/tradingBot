
import sys
import shared.consts as consts
import shared.log as log
import notification.notify as notification
import handlers.positionHandler as positionHandler
import shared.functions as functions
import broker.getters as getters


def isTest():
    arg = sys.argv
    if len(arg) > 1:
        return sys.argv[1] == consts.TEST
    return False


def runTests():
    if isTest():
        TEST_JSON = {"position": "long", "pair": "EURUSD", "time": "15 mins", "time2": "15", "stopLossCanldes": 3,
                     "maxStopLoss": 0.02, "takeProfitRatio": 1.5, "historyDataInterval": "1 D", "alertPrice": 1.5, "alertTime": "10:10:10"}

        connection = notification.openConnection()
        log.info(consts.TEST_RUNNING_MESSAGE)
        positionHandler.handlePosition(connection, TEST_JSON)

        functions.sleep(5)
        msgs = notification.searchUnseenMessages(connection)

        for msg in msgs[0].split():
            subject = notification.fetchMessage(connection, msg)['body']
            testAlertTime = getters.getAlertTime(TEST_JSON)
            if str(subject).find(testAlertTime) > 0:
                log.success("test passed")
            else:
                log.error("test failed")

        sys.exit()
