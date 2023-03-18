
import broker.getters as getters
import shared.consts as consts
import notification.notify as notify


def sendMessage(connection, stopLoss, takeProfit, entry, params):
    position = getters.getPosition(params)
    pair = getters.getPair(params)
    maxStopLoss = getters.getMaxStopLoss(params)
    alertPrice = getters.getAlertPrice(params)

    if maxStopLoss > abs(stopLoss - entry):
        message = getPositionStructure(stopLoss, takeProfit, entry, alertPrice)
        title = getSuccessPositionTitle(position, pair)
    else:
        message = getPositionStructure(stopLoss, takeProfit, entry, alertPrice)
        title = getFailedPositionTitle(position, pair)

    notify.sendMessage(connection, title, message)


def getPositionStructure(stopLoss: float, takeProfit: float, entry: float, alertPrice):
    return "entry =      " + str(entry) + \
        "\n stopLoss =   " + str(stopLoss) + \
        "\n takeProfit = " + str(takeProfit) + \
        "\n alertTirggerPrice = " + str(alertPrice)


def getPositionTitle(positionType: str, pair):
    return positionType + " " + pair


def getSuccessPositionTitle(positionType: str, pair):
    return "Entered " + getPositionTitle(positionType, pair)


def getFailedPositionTitle(positionType: str, pair):
    return "Failed to enter " + getPositionTitle(positionType, pair)