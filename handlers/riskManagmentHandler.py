import shared.consts as consts
import handlers.jsonHandler.getters as getters
import shared.log as log


def getStopLossHistorical(historicalData, params):
    position = getters.getPosition(params)

    match position:
        case consts.LONG:
            stopLoss = getCandlesLow(historicalData)
        case consts.SHORT:
            stopLoss = getCandlesHigh(historicalData)
        case _:
            log.warrning(consts.FAILED_TO_SET_STOP_LOSS_HISTORICAL)
            return 0

    return round(stopLoss, 5)


def getStopLossPercent(params):
    stopLossPercent = getters.getStopLossPercent(params)
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
