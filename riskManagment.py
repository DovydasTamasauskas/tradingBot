
import shared.functions as functions
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

    if getters.isLong(position):
        stopLoss = getCandlesLow(stopLossCandles)
    if getters.isShort(position):
        stopLoss = getCandlesHigh(stopLossCandles)
    return stopLoss


def getTakeProfit(ib, contract, stopLoss, params):
    takeProfitRatio = getters.getTakeProfitRatio(params)
    position = getters.getPosition(params)

    marketPrice = interactiveBrokers.getAskPrice(ib, contract)

    if getters.isLong(position):
        takeProfit = (marketPrice-stopLoss) * takeProfitRatio + marketPrice
    if getters.isShort(position):
        takeProfit = marketPrice-(stopLoss-marketPrice) * takeProfitRatio
    return round(takeProfit, 5)


def getCandlesLow(array):
    return min(list(map(lambda x: x.low, array)))


def getCandlesHigh(array):
    return max(list(map(lambda x: x.high, array)))
