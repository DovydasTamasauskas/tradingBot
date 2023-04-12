import brokers.interactiveBrokers.handlePosition as interactiveBrokers
import notification.gmail as notification
import shared.functions as functions
import scripts

SLEEP_INTERVAL_SEC = 5


def main():
    while True == True:
        connection = notification.openConnection()
        msgs = notification.searchUnseenMessages(connection)

        messages = []
        for msg in msgs[0].split():
            subject = notification.fetchMessage(connection, msg)['subject']
            if functions.isResultMessage(subject) == False:
                subjectJSON = functions.toJson(subject)
                if subjectJSON != None and functions.isRequiredParamsDefined(subjectJSON):
                    messages.append(subjectJSON)

        connection.close()

        for message in messages:
            interactiveBrokers.handlePosition(message)

        functions.sleep(SLEEP_INTERVAL_SEC)


if __name__ == "__main__":
    scripts.scripts()
    main()
