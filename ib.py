from ib_insync import *
import credentials


def getCandlesLow(array):
    return min(list(map(lambda x: x.low, array)))


def getCandlesHigh(array):
    return max(list(map(lambda x: x.high, array)))


def getAskPrice():
    market = ib.reqMktData(contract, '', False, False)
    ib.sleep(2)
    return market.ask


def getHistoricalData():
    return ib.reqHistoricalData(
        contract, endDateTime='', durationStr=HISTORY_DATA_INTERVAL,
        barSizeSetting=TIME_INTERVAL, whatToShow='MIDPOINT', useRTH=True)


def printPosition(stopLoss, takeProfit, entry, positionType):
    if MAX_STOP_LOSS > abs(stopLoss - entry):
        print(positionType)
        print("entry =      "+str(entry))
        print("stopLoss =   "+str(stopLoss))
        print("takeProfit = "+str(takeProfit))
    else:
        print('Position exceded stop loss limit')


# ----------------------------
POSITION_TYPE = "SHORT"
PAIR = 'EURUSD'
STOP_LOSS_CANDLE_COUNT = 3
MAX_STOP_LOSS = 0.02
TIME_INTERVAL = "15 mins"
HISTORY_DATA_INTERVAL = "1 D"
TAKE_PROFIT_RATIO = 1.5
# add to stopLoss??
# ----------------------------
if POSITION_TYPE == "LONG" or POSITION_TYPE == "SHORT":
    ib = IB()
    ib.connect(credentials.IB_HOST, credentials.IB_PORT,
               clientId=credentials.IB_CLIENT_ID)
    contract = Forex(PAIR)

    bars = getHistoricalData()
    marketPrice = getAskPrice()

    if POSITION_TYPE == "LONG":
        stopLoss = getCandlesLow(bars[-STOP_LOSS_CANDLE_COUNT:])
        takeProfit = round((marketPrice-stopLoss) *
                           TAKE_PROFIT_RATIO+marketPrice, 5)

    if POSITION_TYPE == "SHORT":
        stopLoss = getCandlesHigh(bars[-STOP_LOSS_CANDLE_COUNT:])
        takeProfit = round(marketPrice-(stopLoss-marketPrice)
                           * TAKE_PROFIT_RATIO, 5)

    printPosition(stopLoss, takeProfit, marketPrice, POSITION_TYPE)
