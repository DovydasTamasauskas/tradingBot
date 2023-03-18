from . import defaultProps
import shared.consts as consts
import shared.log as log

position = 'position'
pair = 'pair'
time = 'time'
alertPrice = 'alertPrice'
stopLossCanldes = 'stopLossCanldes'
maxStopLoss = 'maxStopLoss'
takeProfitRatio = 'takeProfitRatio'
historyDataInterval = 'historyDataInterval'


def getPosition(params):
    try:
        return params[position]
    except:
        log.error(consts.FAILED_TO_GET_POSITION)


def getPair(params):
    try:
        return params[pair]
    except:
        log.error(consts.FAILED_TO_GET_PAIR)


def getTime(params):
    try:
        return params[time]
    except:
        log.warrning(consts.FAILED_TO_GET_TIME)
        return defaultProps.TIME


def getAlertPrice(params):
    try:
        return params[alertPrice]
    except:
        log.warrning(consts.FAILED_TO_GET_ALERT_TIME)
        return defaultProps.ALERT_TIME


def getStopLossCanldes(params):
    try:
        return params[stopLossCanldes]
    except:
        log.warrning(consts.FAILED_TO_GET_STOPLOSS_CANDLES)
        return defaultProps.STOP_CANDLES_COUNT


def getMaxStopLoss(params):
    try:
        return params[maxStopLoss]
    except:
        log.warrning(consts.FAILED_TO_GET_MAX_STOPLOSS)
        return defaultProps.MAX_STOP_LOSS


def getTakeProfitRatio(params):
    try:
        return params[takeProfitRatio]
    except:
        log.warrning(consts.FAILED_TO_GET_TAKE_PROFIT_RATIO)
        return defaultProps.TAKE_PROFIT_RATIO


def getHistoryDataInterval(params):
    try:
        return params[historyDataInterval]
    except:
        log.warrning(consts.FAILED_TO_GET_HISTORY_DATA_INTERVAL)
        return defaultProps.HISTORY_DATA_INTERVAL
