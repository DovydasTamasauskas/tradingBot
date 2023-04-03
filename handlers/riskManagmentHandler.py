import shared.consts as consts
import handlers.jsonHandler.getters as getters
import shared.log as log


def getStopLoss(historicalData, params):
    stopLossPercent = getters.getStopLossPercent(params)
    position = getters.getPosition(params)
    if stopLossPercent > 0:
        entryPrice = getters.getEnteryPrice(params)
        if isLong(position):
            return entryPrice / 100 * (100 - stopLossPercent)
        if isShort(position):
            return entryPrice / 100 * (100 + stopLossPercent)

    if isLong(position):
        stopLoss = getCandlesLow(historicalData)
    if isShort(position):
        stopLoss = getCandlesHigh(historicalData)

    return stopLoss


def getTakeProfit(params):
    takeProfitRatio = getters.getTakeProfitRatio(params)
    entryPrice = getters.getEnteryPrice(params)
    stopLossPercent = getters.getStopLossPercent(params)

    if stopLossPercent > 0:
        takeProfit = entryPrice / 100 * \
            (100 + stopLossPercent * takeProfitRatio)
    else:
        stopLoss = getters.getStopLoss(params)
        position = getters.getPosition(params)
        if isLong(position):
            takeProfit = (entryPrice-stopLoss) * takeProfitRatio + entryPrice
        else:
            if isShort(position):
                takeProfit = entryPrice-(stopLoss-entryPrice) * takeProfitRatio

    return round(takeProfit, 5)


def getCandlesLow(array):
    try:
        return min(list(map(lambda x: x.low, array)))
    except:
        pass
        # log.error(consts.FAILED_TO_CALCULATE_LOW)


def getCandlesHigh(array):
    try:
        return max(list(map(lambda x: x.high, array)))
    except:
        log.error(consts.FAILED_TO_CALCULATE_HIGH)


def isLong(param):
    return param.lower() == consts.LONG


def isShort(param):
    return param.lower() == consts.SHORT
