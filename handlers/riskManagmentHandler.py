import shared.consts as consts
import handlers.jsonHandler.getters as getters
import shared.log as log
import shared.functions as functions


def isStopLossExceeded(params, stopLoss):
    maxStopLoss = getters.getMaxStopLoss(params)
    entryPrice = getters.getEnteryPrice(params)

    stopLossOnPrice = (100 * stopLoss / entryPrice) - 100

    if maxStopLoss < round(abs(stopLossOnPrice), 1):
        return True
    else:
        return False


def getStopLossHistorical(historicalData, params):
    position = getters.getPosition(params)
    stopLossCanldes = getters.getStopLossCanldes(params)
    maxStopLoss = getters.getMaxStopLoss(params)
    entryPrice = getters.getEnteryPrice(params)
    historicalData = functions.slice(historicalData, -stopLossCanldes)

    match position:
        case consts.LONG:
            stopLoss = getCandlesLow(historicalData)
            if isStopLossExceeded(params, stopLoss):
                stopLoss = 100 * (100 - maxStopLoss) / entryPrice
        case consts.SHORT:
            stopLoss = getCandlesHigh(historicalData)
            if isStopLossExceeded(params, stopLoss):
                stopLoss = 100 * (100 + maxStopLoss) / entryPrice
        case _:
            log.warrning(consts.FAILED_TO_SET_STOP_LOSS_HISTORICAL)
            return 0

    return round(stopLoss, 5)


def getStopLossPercent(params):
    stopLossPercent = getters.getStopLossPercent(params)
    maxStopLoss = getters.getMaxStopLoss(params)
    if stopLossPercent > maxStopLoss:
        stopLossPercent = maxStopLoss
    position = getters.getPosition(params)
    entryPrice = getters.getEnteryPrice(params)

    match position:
        case consts.LONG:
            stopLoss = entryPrice / 100 * (100 - stopLossPercent)
        case consts.SHORT:
            stopLoss = entryPrice / 100 * (100 + stopLossPercent)
        case _:
            log.warrning(consts.FAILED_TO_SET_STOP_LOSS_PERCENT)
            return 0

    return round(stopLoss, 5)


def getTakeProfit(params):
    takeProfitRatio = getters.getTakeProfitRatio(params)
    entryPrice = getters.getEnteryPrice(params)
    stopLoss = getters.getStopLoss(params)

    if entryPrice > stopLoss:
        takeProfit = (entryPrice-stopLoss) * takeProfitRatio + entryPrice
    else:
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
        log.warrning(consts.FAILED_TO_CALCULATE_LOW)


def getCandlesHigh(array):
    try:
        high = 0
        for x in array:
            if high < x['high']:
                high = x['high']
        return high
    except:
        log.warrning(consts.FAILED_TO_CALCULATE_HIGH)
