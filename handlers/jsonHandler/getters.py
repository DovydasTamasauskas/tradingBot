from . import defaultProps
import shared.consts as consts
import shared.log as log

position = 'position'
pair = 'pair'
time = 'time'
size = 'size'
alertPrice = 'alertPrice'
alertTime = 'alertTime'
stopLossCanldes = 'stopLossCanldes'
maxStopLoss = 'maxStopLoss'
takeProfitRatio = 'takeProfitRatio'
historyDataInterval = 'historyDataInterval'
stopLoss = 'stopLoss'
takeProfit = 'takeProfit'
limitPrice = 'limitPrice'
marketPrice = 'marketPrice'
enteryPrice = 'enteryPrice'
stopLossPercent = 'stopLossPercent'
sendResultEmail = 'sendResultEmail'
logEnteredPosition = 'logEnteredPosition'


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


def getSize(params):
    try:
        return params[size]
    except:
        log.warrning(consts.FAILED_TO_SIZE)
        return defaultProps.SIZE


def getAlertPrice(params):
    try:
        return params[alertPrice]
    except:
        # log.warrning(consts.FAILED_TO_GET_ALERT_PRICE)
        return None


def getAlertTime(params):
    try:
        return params[alertTime]
    except:
        # log.warrning(consts.FAILED_TO_GET_ALERT_TIME)
        return None


def getStopLossCanldes(params):
    try:
        return params[stopLossCanldes]
    except:
        # log.warrning(consts.FAILED_TO_GET_STOPLOSS_CANDLES)
        return None


def getMaxStopLoss(params):
    try:
        return params[maxStopLoss]
    except:
        # log.warrning(consts.FAILED_TO_GET_MAX_STOPLOSS)
        return None


def getTakeProfitRatio(params):
    try:
        return params[takeProfitRatio]
    except:
        # log.warrning(consts.FAILED_TO_GET_TAKE_PROFIT_RATIO)
        return defaultProps.TAKE_PROFIT_RATIO


def getHistoryDataInterval(params):
    try:
        return params[historyDataInterval]
    except:
        log.warrning(consts.FAILED_TO_GET_HISTORY_DATA_INTERVAL)
        return defaultProps.HISTORY_DATA_INTERVAL


def getStopLoss(params):
    try:
        return params[stopLoss]
    except:
        log.warrning(consts.FAILED_TO_GET_STOP_LOSS)
        return 0


def getTakeProfit(params):
    try:
        return params[takeProfit]
    except:
        log.warrning(consts.FAILED_TO_GET_TAKE_PROFIT)
        return 0


def getLimitPrice(params):
    try:
        return params[limitPrice]
    except:
        return 0


def getMarketPrice(params):
    try:
        return params[marketPrice]
    except:
        log.warrning(consts.FAILED_TO_GET_MARKET_PRICE)
        return 0


def getEnteryPrice(params):
    try:
        return params[enteryPrice]
    except:
        log.error(consts.FAILED_TO_GET_ENTRY_PRICE)
        return 0


def getStopLossPercent(params):
    try:
        return params[stopLossPercent]
    except:
        return 0


def getSendResultEmail(params):
    try:
        return params[sendResultEmail]
    except:
        return True


def getLogEnteredPosition(params):
    try:
        return params[logEnteredPosition]
    except:
        return True
