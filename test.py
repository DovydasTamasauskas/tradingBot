
import sys
import shared.log as log
import notification.notify as notification
import brokers.interactiveBrokers.handlePosition as interactiveBrokers
import shared.functions as functions
import handlers.jsonHandler.getters as getters
import testHeplers as heplers
import json


def test1():
    heplers.testTitle("TakeProfit and stopLoss should be calculated correctly")
    resultJSON = interactiveBrokers.handlePosition(heplers.createJson())

    stopLoss = getters.getStopLoss(resultJSON)
    takeProfit = getters.getTakeProfit(resultJSON)
    if stopLoss == 98 and takeProfit == 103:
        log.success("test passed")
    else:
        log.error("test failed")


def test11():
    heplers.testTitle("stopLoss should be calculated correctly")
    resultJSON = interactiveBrokers.handlePosition(heplers.createJson())

    stopLoss = getters.getStopLoss(resultJSON)
    if stopLoss == 98:
        log.success("test passed")
    else:
        log.error("test failed")


def test12():
    heplers.testTitle("takeProfit should be calculated correctly")
    resultJSON = interactiveBrokers.handlePosition(heplers.createJson())

    takeProfit = getters.getTakeProfit(resultJSON)
    if takeProfit == 103:
        log.success("test passed")
    else:
        log.error("test failed")


def test3():
    heplers.testTitle("Email and code integration test")

    TEST_JSON = heplers.createJson()
    TEST_JSON_STR = json.dumps(TEST_JSON)

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
    if heplers.isTest():
        test1()
        test11()
        test12()
        test3()
        sys.exit()
