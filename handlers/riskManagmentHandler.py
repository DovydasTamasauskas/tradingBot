
import shared.functions as functions
import shared.consts as consts
import broker.interactiveBrokers as interactiveBrokers
import broker.getters as getters


def getStopLoss(ib, contract, params):
    stopLossCanldes = getters.getStopLossCanldes(params)
    time = getters.getTime(params)
    historicalDataInterval = getters.getHistoryDataInterval(params)
    position = getters.getPosition(params)

    historicalData = interactiveBrokers.getHistoricalData(
        ib, contract, time, historicalDataInterval)
    stopLossCandles = functions.slice(historicalData, -stopLossCanldes)

    if isLong(position):
        stopLoss = getCandlesLow(stopLossCandles)
    if isShort(position):
        stopLoss = getCandlesHigh(stopLossCandles)

    return stopLoss


def getTakeProfit(stopLoss, marketPrice, params):
    takeProfitRatio = getters.getTakeProfitRatio(params)
    position = getters.getPosition(params)

    if isLong(position):
        takeProfit = (marketPrice-stopLoss) * takeProfitRatio + marketPrice
    if isShort(position):
        takeProfit = marketPrice-(stopLoss-marketPrice) * takeProfitRatio

    return round(takeProfit, 5)


def getCandlesLow(array):
    return min(list(map(lambda x: x.low, array)))


def getCandlesHigh(array):
    return max(list(map(lambda x: x.high, array)))


def isLong(param):
    return param.lower() == consts.LONG


def isShort(param):
    return param.lower() == consts.SHORT
