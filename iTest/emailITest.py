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

    connection = notification.openConnection()
    notification.sendMail("Title", str(TEST_JSON_STR))
    connection.close()

    functions.sleep(5)

    connection = notification.openConnection()
    msgs = notification.searchUnseenMessages(connection)

    messages = []
    if msgs != None:
        for msg in msgs[0].split():
            subject = notification.fetchMessage(connection, msg)[consts.BODY]
            if functions.isResultMessage(subject) == False:
                subjectJSON = functions.toJson(subject)
                messages.append(subjectJSON)

        for message in messages:
            if message == TEST_JSON:
                log.success("test passed")
                return 0

    connection.close()
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
