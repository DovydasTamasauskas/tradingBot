import brokers.interactiveBrokers.handlePosition as interactiveBrokers
import notification.gmail as notification
import shared.functions as functions
import scripts
import brokers.kraken.handlePosition as krakenHandler
import notification.helpers.messages as notifyHelper
import handlers.jsonHandler.getters as getters
import shared.consts as consts

SLEEP_INTERVAL_SEC = 5


def main():
    while True == True:
        messages = notification.searchUnseenMessages()
        for message in messages:
            if getters.getBroker(message) == consts.INTERACTIVE_BROKERS:
                interactiveBrokers.handlePosition(
                    message)
            else:
                krakenHandler.handlePosition(message)

        krakenHandler.removeInvalideOrders()
        functions.sleep(SLEEP_INTERVAL_SEC)


if __name__ == "__main__":
    scripts.scripts()
    main()
