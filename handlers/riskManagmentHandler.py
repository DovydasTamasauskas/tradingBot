import shared.consts as consts
import handlers.jsonHandler.getters as getters
import shared.log as log


def getStopLossHistorical(historicalData, params):
    position = getters.getPosition(params)

    if isLong(position):
        stopLoss = getCandlesLow(historicalData)
    if isShort(position):
        stopLoss = getCandlesHigh(historicalData)

    return round(stopLoss, 5)


def getStopLossPercent(params):
    stopLossPercent = getters.getStopLossPercent(params)
    position = getters.getPosition(params)
    if stopLossPercent > 0:
        entryPrice = getters.getEnteryPrice(params)
        if isLong(position):
            return entryPrice / 100 * (100 - stopLossPercent)
        if isShort(position):
            return entryPrice / 100 * (100 + stopLossPercent)

    log.warrning(consts.FAILED_TO_SET_STOP_LOSS_PERCENT)
    return 0


def getTakeProfit(params):
    takeProfitRatio = getters.getTakeProfitRatio(params)
    entryPrice = getters.getEnteryPrice(params)
    stopLoss = getters.getStopLoss(params)

    if entryPrice > stopLoss:
        takeProfit = (entryPrice-stopLoss) * takeProfitRatio + entryPrice
    if entryPrice < stopLoss:
        takeProfit = entryPrice-(stopLoss-entryPrice) * takeProfitRatio

    return round(takeProfit, 5)


def getCandlesLow(array):
    try:
        low = 100000
        for x in array:
            if low > x['low']:
                low = x['low']
        return low
    except:
        pass
        # log.error(consts.FAILED_TO_CALCULATE_LOW)


def getCandlesHigh(array):
    try:
        high = 0
        for x in array:
            if high < x['high']:
                high = x['high']
        return high
    except:
        log.error(consts.FAILED_TO_CALCULATE_HIGH)


def isLong(param):
    return param.lower() == consts.LONG


def isShort(param):
    return param.lower() == consts.SHORT
