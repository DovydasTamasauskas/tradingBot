
import shared.consts as consts
from . import defaultProps
import shared.log as log


enterPrice = 'enterPrice'
stopLosss = 'stopLosss'
takeProfit = 'takeProfit'
enterTime = 'enterTime'


def setEnterPrice(params, value):
    try:
        params[enterPrice] = value
        return params
    except:
        log.warrning(consts.FAILED_TO_SET_ENTER_PRICE)
        return defaultProps.ENTER_PRICE


def setStopLoss(params, value):
    try:
        params[stopLosss] = value
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
