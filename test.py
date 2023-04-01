
import sys
import shared.consts as consts
import shared.log as log
import notification.notify as notification
import brokers.interactiveBrokers.handlePosition as interactiveBrokers
import shared.functions as functions
import handlers.jsonHandler.getters as getters
import json


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

    print('- ' * 20)
    log.info(consts.TEST_RUNNING_MESSAGE)
    log.info("TakeProfit and stopLoss should be calculated correctly")
    resultJSON = interactiveBrokers.handlePosition(TEST_JSON)

    stopLoss = getters.getStopLoss(resultJSON)
    takeProfit = getters.getTakeProfit(resultJSON)
    if stopLoss == 98 and takeProfit == 103:
        log.success("test passed")
    else:
        log.error("test failed")


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

    print('- ' * 20)
    log.info(consts.TEST_RUNNING_MESSAGE)
    log.info("stopLoss should be calculated correctly")
    resultJSON = interactiveBrokers.handlePosition(TEST_JSON)

    stopLoss = getters.getStopLoss(resultJSON)
    if stopLoss == 98:
        log.success("test passed")
    else:
        log.error("test failed")


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

    print('- ' * 20)
    log.info(consts.TEST_RUNNING_MESSAGE)
    log.info("takeProfit should be calculated correctly")
    resultJSON = interactiveBrokers.handlePosition(TEST_JSON)

    takeProfit = getters.getTakeProfit(resultJSON)
    if takeProfit == 103:
        log.success("test passed")
    else:
        log.error("test failed")


def test2():
    TEST_JSON = {
        "position": "long",
        "pair": "EURUSD",
        "size": 100,
        "time": "15 mins",
        "time2": "15",
        "stopLossCanldes": 3,
        "maxStopLoss": 0.02,
        "takeProfitRatio": 1.5,
        "historyDataInterval": "1 D",
        "alertPrice": 1.5,
        "alertTime": "10:10:10",
        "limitPrice": 1.0,
        "stopLossPercent": 1
    }
    connection = notification.openConnection()
    print('- ' * 20)
    log.info(consts.TEST_RUNNING_MESSAGE)
    log.info("Email body should be correct")
    positionData = interactiveBrokers.handlePosition(TEST_JSON)
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


def test3():
    TEST_JSON = {
        "position": "long",
        "pair": "EURUSD",
        "size": 100,
        "time": "15 mins",
        "time2": "15",
        "stopLossCanldes": 3,
        "maxStopLoss": 0.02,
        "takeProfitRatio": 1.5,
        "historyDataInterval": "1 D",
        "alertPrice": 1.5,
        "alertTime": "10:10:10",
        "limitPrice": 1.0,
        "stopLossPercent": 1
    }

    TEST_JSON_STR = json.dumps(TEST_JSON)
    print('- ' * 20)
    log.info(consts.TEST_RUNNING_MESSAGE)
    log.info("Email and code integration test")

    connection = notification.openConnection()
    notification.sendMail(str(TEST_JSON_STR), str(TEST_JSON_STR))
    connection.close()

    functions.sleep(5)

    connection = notification.openConnection()
    msgs = notification.searchUnseenMessages(connection)

    messages = []
    for msg in msgs[0].split():
        subject = notification.fetchMessage(connection, msg)['subject']
        if functions.isResultMessage(subject) == False:
            subjectJSON = functions.toJson(subject)
            messages.append(subjectJSON)

    connection.close()

    for message in messages:
        if message == TEST_JSON:
            log.success("test passed")
            return 0

    log.error("test failed")


def runTests():
    if isTest():
        test1()
        test11()
        test12()
        # test2()
        test3()
        sys.exit()
