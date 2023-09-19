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
    notification.sendMail("Title", str(TEST_JSON_STR))
    connection.close()


def sendEmailBTC():
    heplers.testTitle("Sending email")
    TEST_JSON = heplers.createJson(
        position='long',
        pair="XXBTZUSD",
        size=0.01,
        stopLossCanldes=4,
        time='5 mins',
        logEnteredPosition=True,
        sendResultEmail=True
    )

    TEST_JSON_STR = json.dumps(TEST_JSON)

    connection = notification.openConnection()
    notification.sendMail("Title", str(TEST_JSON_STR))
    connection.close()
