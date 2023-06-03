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


def getMaxStopLossByPercent(params):
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


def getStopLoss(p, stopLossByCandle):
    realStopLossCanldes = getters.getRealStopLossCanldes(p)

    if realStopLossCanldes == 0:
        stopLoss = getMaxStopLossByPercent(p)
    else:
        stopLoss = stopLossByCandle
        if isStopLossExceeded(p, stopLoss):
            stopLoss = getMaxStopLossByPercent(p)

    return stopLoss
