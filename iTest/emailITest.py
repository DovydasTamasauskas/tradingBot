import shared.log as log
import notification.notify as notification
import shared.functions as functions
import iTest.heplers as heplers
import json


def EmailITest():
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
    EmailITest()
