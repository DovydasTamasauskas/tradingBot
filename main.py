import brokers.interactiveBrokers.handlePosition as interactiveBrokers
import notification.gmail as notification
import shared.functions as functions
import scripts
import brokers.kraken.handlePosition as krakenHandler
import notification.helpers.messages as notifyHelper

SLEEP_INTERVAL_SEC = 5


def main():
    while True == True:
        connection = notification.openConnection()
        msgs = notification.searchUnseenMessages(connection)

        messages = []
        if msgs != None:
            for msg in msgs[0].split():
                subject = notification.fetchMessage(connection, msg)['subject']
                if functions.isResultMessage(subject) == False:
                    subjectJSON = functions.toJson(subject)
                    if subjectJSON != None and functions.isRequiredParamsDefined(subjectJSON):
                        messages.append(subjectJSON)

            for message in messages:
                # positionResults = interactiveBrokers.handlePosition(message)
                positionResults = krakenHandler.handlePosition(message)
                if positionResults != None:
                    notifyHelper.sendEmail(positionResults)
                    notifyHelper.printToConsole(positionResults)

            positionResults = krakenHandler.removeInvalideOrders()

        connection.close()
        functions.sleep(SLEEP_INTERVAL_SEC)


if __name__ == "__main__":
    scripts.scripts()
    main()
