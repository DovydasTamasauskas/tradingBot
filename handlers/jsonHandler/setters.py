
import shared.consts as consts
from . import defaultProps
import shared.log as log


enteryPrice = 'enteryPrice'
stopLoss = 'stopLoss'
takeProfit = 'takeProfit'
enterTime = 'enterTime'
marketPrice = 'marketPrice'


def setEnteryPrice(params, value):
    try:
        params[enteryPrice] = value
        return params
    except:
        log.warrning(consts.FAILED_TO_SET_ENTER_PRICE)
        return defaultProps.ENTER_PRICE


def setStopLoss(params, value):
    try:
        params[stopLoss] = value
        return params
    except:
        log.warrning(consts.FAILED_TO_SET_STOP_LOSS)
        return defaultProps.STOP_LOSS


def setTakeProfit(params, value):
    try:
        params[takeProfit] = value
        return params
    except:
        log.warrning(consts.FAILED_TO_SET_TAKE_PROFIT)
        return defaultProps.TAKE_PROFIT


def setEnterTime(params, value):
    try:
        params[enterTime] = value
        return params
    except:
        log.warrning(consts.FAILED_TO_SET_ENTER_TIME)
        return defaultProps.ENTER_TIME


def setMarketPrice(params, value):
    try:
        params[marketPrice] = value
        return params
    except:
        log.warrning(consts.FAILED_TO_SET_MARKET_PRICE)
        return defaultProps.MARKET_PRICE
