
import sys
import shared.consts as consts
import shared.log as log
import notification.notify as notification
import brokers.interactiveBrokers.handlePosition as interactiveBrokers
import shared.functions as functions
import handlers.jsonHandler.getters as getters


def isTest():
    arg = sys.argv
    if len(arg) > 1:
        return sys.argv[1] == consts.TEST
    return False


def test1():
    TEST_JSON = {
        "position": "long",
        "pair": "EURUSD",
        "size": 100,
        "time": "15 mins",
        "time2": "15",
        "stopLossCanldes": 3,
        "maxStopLoss": 100,
        "takeProfitRatio": 1.5,
        "historyDataInterval": "1 D",
        "alertPrice": 1.5,
        "alertTime": "10:10:10",
        "limitPrice": 100.0,
        "stopLossPercent": 2
    }

    connection = notification.openConnection()
    log.info(consts.TEST_RUNNING_MESSAGE)
    log.info("TakeProfit and stopLoss should be calculated correctly")
    interactiveBrokers.handlePosition(connection, TEST_JSON)

    functions.sleep(5)
    msgs = notification.searchUnseenMessages(connection)

    for msg in msgs[0].split():
        encodedResponse = notification.fetchMessage(connection, msg)['body']
        response = functions.decodeJson(encodedResponse)
        stopLoss = getters.getStopLoss(response)
        takeProfit = getters.getTakeProfit(response)
        if stopLoss == 98 and takeProfit == 103:
            log.success("test passed")
        else:
            log.error("test failed")

    connection.close()


def test11():
    TEST_JSON = {
        "position": "long",
        "pair": "EURUSD",
        "size": 100,
        "time": "15 mins",
        "time2": "15",
        "stopLossCanldes": 3,
        "maxStopLoss": 100,
        "takeProfitRatio": 1.5,
        "historyDataInterval": "1 D",
        "alertPrice": 1.5,
        "alertTime": "10:10:10",
        "limitPrice": 100.0,
        "stopLossPercent": 2
    }

    connection = notification.openConnection()
    log.info(consts.TEST_RUNNING_MESSAGE)
    log.info("stopLoss should be calculated correctly")
    interactiveBrokers.handlePosition(connection, TEST_JSON)

    functions.sleep(5)
    msgs = notification.searchUnseenMessages(connection)

    for msg in msgs[0].split():
        encodedResponse = notification.fetchMessage(connection, msg)['body']
        response = functions.decodeJson(encodedResponse)
        stopLoss = getters.getStopLoss(response)
        if stopLoss == 98:
            log.success("test passed")
        else:
            log.error("test failed")

    connection.close()


def test12():
    TEST_JSON = {
        "position": "long",
        "pair": "EURUSD",
        "size": 100,
        "time": "15 mins",
        "time2": "15",
        "stopLossCanldes": 3,
        "maxStopLoss": 100,
        "takeProfitRatio": 1.5,
        "historyDataInterval": "1 D",
        "alertPrice": 1.5,
        "alertTime": "10:10:10",
        "limitPrice": 100.0,
        "stopLossPercent": 2
    }

    connection = notification.openConnection()
    log.info(consts.TEST_RUNNING_MESSAGE)
    log.info("takeProfit should be calculated correctly")
    interactiveBrokers.handlePosition(connection, TEST_JSON)

    functions.sleep(5)
    msgs = notification.searchUnseenMessages(connection)

    for msg in msgs[0].split():
        encodedResponse = notification.fetchMessage(connection, msg)['body']
        response = functions.decodeJson(encodedResponse)
        takeProfit = getters.getTakeProfit(response)
        if takeProfit == 103:
            log.success("test passed")
        else:
            log.error("test failed")

    connection.close()


def test2():
    TEST_JSON = {"position": "long", "pair": "EURUSD", "size": 100, "time": "15 mins", "time2": "15", "stopLossCanldes": 3,
                 "maxStopLoss": 0.02, "takeProfitRatio": 1.5, "historyDataInterval": "1 D", "alertPrice": 1.5, "alertTime": "10:10:10", "limitPrice": 1.0, "stopLossPercent": 1}

    connection = notification.openConnection()
    log.info(consts.TEST_RUNNING_MESSAGE)
    log.info("Email body should be correct")
    positionData = interactiveBrokers.handlePosition(connection, TEST_JSON)
    functions.sleep(5)
    msgs = notification.searchUnseenMessages(connection)

    for msg in msgs[0].split():
        encodedResponse = notification.fetchMessage(connection, msg)['body']
        response = functions.decodeJson(encodedResponse)
        if response == positionData:
            log.success("test passed")
        else:
            log.error("test failed")

    connection.close()


def runTests():
    if isTest():
        test1()
        test11()
        test12()
        test2()
        sys.exit()


# print('- ' * 20)
