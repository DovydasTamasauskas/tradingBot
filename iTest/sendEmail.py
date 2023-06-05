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


def sendEmail2():
    heplers.testTitle("Sending email")
    TEST_JSON = heplers.createJson(
        position='short',
        # limitPrice=1.07,
        pair="EURUSD",
        size=0.0001,
        time='15 mins',
        stopLossCanldes=4,
        logEnteredPosition=True
    )

    TEST_JSON_STR = json.dumps(TEST_JSON)

    connection = notification.openConnection()
    notification.sendMail(str(TEST_JSON_STR), str(TEST_JSON_STR))
    connection.close()
