
import shared.functions as functions
import shared.consts as consts
import broker.interactiveBrokers as interactiveBrokers
import broker.getters as getters
import shared.log as log


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
    try:
        return min(list(map(lambda x: x.low, array)))
    except:
        log.error(consts.FAILED_TO_CALCULATE_LOW)


def getCandlesHigh(array):
    try:
        return max(list(map(lambda x: x.high, array)))
    except:
        log.error(consts.FAILED_TO_CALCULATE_HIGH)


def isLong(param):
    return param.lower() == consts.LONG


def isShort(param):
    return param.lower() == consts.SHORT
