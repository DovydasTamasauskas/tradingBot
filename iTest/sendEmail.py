import shared.log as log
import notification.notify as notification
import brokers.interactiveBrokers.handlePosition as interactiveBrokers
import shared.functions as functions
import iTest.heplers as heplers
import json


def sendEmail():
    heplers.testTitle("Sending email")

    TEST_JSON = heplers.createJson(
        sendResultEmail=True, logEnteredPosition=True)
    TEST_JSON_STR = json.dumps(TEST_JSON)

    connection = notification.openConnection()
    notification.sendMail(str(TEST_JSON_STR), str(TEST_JSON_STR))
    connection.close()
