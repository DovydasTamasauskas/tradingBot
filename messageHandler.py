import notification.notify as notify
import broker.interactiveBrokers as interactiveBrokers
import broker.getters as getters
import broker.defaultProps as defaultProps
import shared.messages as messages
import shared.functions as functions


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


def main(connection, p):
    ib = interactiveBrokers.openIbConnection()

    pair = getters.getPair(p)
    contract = interactiveBrokers.setContract(pair)

    historicalData = interactiveBrokers.getHistoricalData(
        ib, contract, getters.getTime(p), getters.getHistoryDataInterval(p))
    marketPrice = interactiveBrokers.getAskPrice(ib, contract)

    if historicalData != None and marketPrice != None:
        stopLossCanldes = getters.getStopLossCanldes(p)
        takeProfitRatio = getters.getTakeProfitRatio(p)
        stopLossCandles = functions.slice(historicalData, -stopLossCanldes)

        position = getters.getPosition(p)
        if getters.isLong(position):
            stopLoss = getCandlesLow(stopLossCandles)
            takeProfit = (marketPrice-stopLoss) * takeProfitRatio + marketPrice

        if getters.isShort(position):
            stopLoss = getCandlesHigh(stopLossCandles)
            takeProfit = marketPrice-(stopLoss-marketPrice) * takeProfitRatio

        takeProfit = round(takeProfit, 5)
        sendMessage(connection, stopLoss, takeProfit,
                    marketPrice, position, pair, getters.getMaxStopLoss(p))
