import notification.notify as notify
import broker.interactiveBrokers as interactiveBrokers
from . import getters
from . import defaultProps
from . import messages


def getCandlesLow(array):
    return min(list(map(lambda x: x.low, array)))


def getCandlesHigh(array):
    return max(list(map(lambda x: x.high, array)))


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


def isLong(param: str):
    return param.lower() == defaultProps.LONG


def isShort(param: str):
    return param.lower() == defaultProps.SHORT


def slice(val: str, start=0, end=None):
    return val[start:end]


def main(connection, p):
    position = getters.getPosition(p)
    if isLong(position) or isShort(position):
        ib = interactiveBrokers.openIbConnection()

        pair = getters.getPair(p)
        contract = interactiveBrokers.setContract(pair)

        bars = interactiveBrokers.getHistoricalData(
            ib, contract, getters.getTime(p), getters.getHistoryDataInterval(p))
        marketPrice = interactiveBrokers.getAskPrice(ib, contract)

        if bars != None and marketPrice != None:
            stopLossCanldes = getters.getStopLossCanldes(p)
            takeProfitRatio = getters.getTakeProfitRatio(p)
            if isLong(position):
                stopLoss = getCandlesLow(slice(bars, -stopLossCanldes))
                takeProfit = round((marketPrice-stopLoss) *
                                   takeProfitRatio+marketPrice, 5)

            if isShort(position):
                stopLoss = getCandlesHigh(slice(bars, -stopLossCanldes))
                takeProfit = round(marketPrice-(stopLoss-marketPrice)
                                   * takeProfitRatio, 5)

            sendMessage(connection, stopLoss, takeProfit,
                        marketPrice, position, pair, getters.getMaxStopLoss(p))
