
import broker.getters as getters
import shared.messages as messages
import notification.notify as notify


def sendMessage(connection, stopLoss, takeProfit, entry, params):

    position = getters.getPosition(params)
    pair = getters.getPair(params)
    maxStopLoss = getters.getMaxStopLoss(params)
    if maxStopLoss > abs(stopLoss - entry):
        message = getPositionStructure(stopLoss, takeProfit, entry)
        title = getSuccessPositionTitle(position, pair)
    else:
        message = messages.EXEDED_STOPLOSS_LIMIT
        title = getFailedPositionTitle(position, pair)
    notify.sendMessage(connection, title, message)


def getPositionStructure(stopLoss: float, takeProfit: float, entry: float):
    return "entry =      " + str(entry) + \
        "\n stopLoss =   " + str(stopLoss) + \
        "\n takeProfit = " + str(takeProfit)


def getPositionTitle(positionType: str, pair):
    return positionType + " " + pair


def getSuccessPositionTitle(positionType: str, pair):
    return "Entered " + getPositionTitle(positionType, pair)


def getFailedPositionTitle(positionType: str, pair):
    return "Failed to enter " + getPositionTitle(positionType, pair)
