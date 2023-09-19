import shared.log as log
import notification.gmail as notification
import brokers.interactiveBrokers.handlePosition as interactiveBrokers
import shared.functions as functions
import iTest.heplers as heplers
import json
import shared.consts as consts


def EmailITest():
    heplers.testTitle("Gmail and code integration test")

    TEST_JSON = heplers.createJson()
    TEST_JSON_STR = json.dumps(TEST_JSON)

    notification.sendMail("Title", str(TEST_JSON_STR))

    functions.sleep(5)

    messages = notification.searchUnseenMessages()

    for message in messages:
        if message == TEST_JSON:
            log.success("test passed")
            return 0

    log.error("test failed")


def EmailResultsITest():
    heplers.testTitle("Form results correctly")

    TEST_JSON = heplers.createJson(sendResultEmail=True, pair="AUDUSD")
    positionResults = interactiveBrokers.handlePosition(TEST_JSON)

    if positionResults["pair"] == "AUDUSD":
        log.success("test passed")
        return 0

    log.error("test failed")


def runTests():
    EmailITest()
    EmailResultsITest()
