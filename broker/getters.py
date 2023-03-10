from . import defaultProps

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
        return defaultProps.POSITION


def getPair(params):
    try:
        return params[pair]
    except:
        return defaultProps.PAIR


def getTime(params):
    try:
        return params[time]
    except:
        return defaultProps.TIME


def getStopLossCanldes(params):
    try:
        return params[stopLossCanldes]
    except:
        return defaultProps.STOP_CANDLES_COUNT


def getMaxStopLoss(params):
    try:
        return params[maxStopLoss]
    except:
        return defaultProps.MAX_STOP_LOSS


def getTakeProfitRatio(params):
    try:
        return params[takeProfitRatio]
    except:
        return defaultProps.TAKE_PROFIT_RATIO


def getHistoryDataInterval(params):
    try:
        return params[historyDataInterval]
    except:
        return defaultProps.HISTORY_DATA_INTERVAL
