import notification.notify as notify
import broker.interactiveBrokers as interactiveBrokers
import broker.getters as getters
import shared.messages as messages
import riskManagment


def sendMessage(connection, stopLoss, takeProfit, entry, positionType, pair, maxStopLoss):
    if maxStopLoss > abs(stopLoss - entry):
        message = getPositionStructure(stopLoss, takeProfit, entry)
        title = getSuccessPositionTitle(positionType, pair)
    else:
        message = messages.EXEDED_STOPLOSS_LIMIT
        title = getFailedPositionTitle(positionType, pair)
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


def main(connection, p):
    ib = interactiveBrokers.openIbConnection()

    pair = getters.getPair(p)
    contract = interactiveBrokers.setContract(pair)

    marketPrice = interactiveBrokers.getAskPrice(ib, contract)

    position = getters.getPosition(p)
    stopLoss = riskManagment.getStopLoss(ib, contract, p)
    takeProfit = riskManagment.getTakeProfit(ib, contract, stopLoss, p)

    sendMessage(connection, stopLoss, takeProfit,
                marketPrice, position, pair, getters.getMaxStopLoss(p))
