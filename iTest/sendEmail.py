import notification.gmail as notification
import iTest.heplers as heplers
import json


def sendEmail():
    heplers.testTitle("Sending email")
    TEST_JSON = heplers.createJson(
        position='long',
        # limitPrice=1.07,
        pair="EURUSD",
        size=100,
        time='15 mins',
        stopLossCanldes=4,
        logEnteredPosition=True
    )

    TEST_JSON_STR = json.dumps(TEST_JSON)

    connection = notification.openConnection()
    notification.sendMail(str(TEST_JSON_STR), str(TEST_JSON_STR))
    connection.close()


def sendEmailBTC():
    heplers.testTitle("Sending email")
    TEST_JSON = heplers.createJson(
        position='short',
        pair="XXBTZUSD",
        size=0.0001,
        stopLossCanldes=4,
        logEnteredPosition=True
    )

    TEST_JSON_STR = json.dumps(TEST_JSON)

    connection = notification.openConnection()
    notification.sendMail(str(TEST_JSON_STR), str(TEST_JSON_STR))
    connection.close()
