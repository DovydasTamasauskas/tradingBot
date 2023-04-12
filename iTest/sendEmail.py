import shared.log as log
import notification.gmail as notification
import brokers.interactiveBrokers.handlePosition as interactiveBrokers
import shared.functions as functions
import iTest.heplers as heplers
import json


def sendEmail():
    heplers.testTitle("Sending email")

    TEST_JSON = {
        "position": "long",
        "pair": "EURUSD",
        "size": 100,
        "time": "15 mins",
    }
    TEST_JSON_STR = json.dumps(TEST_JSON)

    connection = notification.openConnection()
    notification.sendMail(str(TEST_JSON_STR), str(TEST_JSON_STR))
    connection.close()
