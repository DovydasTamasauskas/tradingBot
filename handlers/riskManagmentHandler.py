
import shared.functions as functions
import shared.consts as consts
import brokers.interactiveBrokers.api as api
import handlers.jsonHandler.getters as getters
import shared.log as log


def getStopLoss(ib, contract, params):

    stopLossPercent = getters.getStopLossPercent(params)
    if stopLossPercent > 0:
        entryPrice = getters.getEnteryPrice(params)
        return entryPrice / 100 * (100 - stopLossPercent)

    stopLossCanldes = getters.getStopLossCanldes(params)
    time = getters.getTime(params)
    historicalDataInterval = getters.getHistoryDataInterval(params)
    position = getters.getPosition(params)

    historicalData = api.getHistoricalData(
        ib, contract, time, historicalDataInterval)
    stopLossCandles = functions.slice(historicalData, -stopLossCanldes)

    if isLong(position):
        stopLoss = getCandlesLow(stopLossCandles)
    if isShort(position):
        stopLoss = getCandlesHigh(stopLossCandles)

    return stopLoss


def getTakeProfit(params):
    takeProfitRatio = getters.getTakeProfitRatio(params)
    position = getters.getPosition(params)
    entryPrice = getters.getEnteryPrice(params)
    stopLoss = getters.getStopLoss(params)

    if isLong(position):
        takeProfit = (entryPrice-stopLoss) * takeProfitRatio + entryPrice
    if isShort(position):
        takeProfit = entryPrice-(stopLoss-entryPrice) * takeProfitRatio

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
