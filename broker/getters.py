from . import defaultProps
import shared.consts as consts
import shared.functions as functions
import sys

position = 'position'
pair = 'pair'
time = 'time'
stopLossCanldes = 'stopLossCanldes'
maxStopLoss = 'maxStopLoss'
takeProfitRatio = 'takeProfitRatio'
historyDataInterval = 'historyDataInterval'


def getPosition(params):
    try:
        return params[position]
    except:
        functions.error(consts.FAILED_TO_GET_POSITION)
        sys.exit()


def getPair(params):
    try:
        return params[pair]
    except:
        functions.error(consts.FAILED_TO_GET_PAIR)
        sys.exit()


def getTime(params):
    try:
        return params[time]
    except:
        functions.warrning(consts.FAILED_TO_GET_TIME)
        return defaultProps.TIME


def getStopLossCanldes(params):
    try:
        return params[stopLossCanldes]
    except:
        functions.warrning(consts.FAILED_TO_GET_STOPLOSS_CANDLES)
        return defaultProps.STOP_CANDLES_COUNT


def getMaxStopLoss(params):
    try:
        return params[maxStopLoss]
    except:
        functions.warrning(consts.FAILED_TO_GET_MAX_STOPLOSS)
        return defaultProps.MAX_STOP_LOSS


def getTakeProfitRatio(params):
    try:
        return params[takeProfitRatio]
    except:
        functions.warrning(consts.FAILED_TO_GET_TAKE_PROFIT_RATIO)
        return defaultProps.TAKE_PROFIT_RATIO


def getHistoryDataInterval(params):
    try:
        return params[historyDataInterval]
    except:
        functions.warrning(consts.FAILED_TO_GET_HISTORY_DATA_INTERVAL)
        return defaultProps.HISTORY_DATA_INTERVAL
