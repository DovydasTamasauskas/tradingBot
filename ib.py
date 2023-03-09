from ib_insync import *
import credentials
import send


def getCandlesLow(array):
    return min(list(map(lambda x: x.low, array)))


def getCandlesHigh(array):
    return max(list(map(lambda x: x.high, array)))


def getAskPrice(ib, contract):
    market = ib.reqMktData(contract, '', False, False)
    ib.sleep(2)
    return market.ask


def getHistoricalData(ib, contract):
    return ib.reqHistoricalData(
        contract, endDateTime='', durationStr=HISTORY_DATA_INTERVAL,
        barSizeSetting=TIME_INTERVAL, whatToShow='MIDPOINT', useRTH=True)


def sendMessage(connection, stopLoss, takeProfit, entry, positionType, pair):
    if MAX_STOP_LOSS > abs(stopLoss - entry):
        message = getPositionStructure(stopLoss, takeProfit, entry)
        title = getSuccessPositionTitle(positionType, pair)
    else:
        message = "Exceded stopLoss limit"
        title = getFailedPositionTitle(positionType, pair)
    send.sendMessage(connection, title, message)


def getPositionStructure(stopLoss, takeProfit, entry):
    return "entry =      " + \
        str(entry)+"\n stopLoss =   "+str(stopLoss) + \
        "\n takeProfit = "+str(takeProfit)


def getPositionTitle(positionType, pair):
    return positionType + " " + pair


def getSuccessPositionTitle(positionType, pair):
    return "Entered " + getPositionTitle(positionType, pair)


def getFailedPositionTitle(positionType, pair):
    return "Failed to enter " + getPositionTitle(positionType, pair)


def isLong(param):
    return param.lower() == 'long'


def isShort(param):
    return param.lower() == 'short'


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


def main(connection, POSITION_TYPE="SHORT", PAIR='EURUSD',
         STOP_LOSS_CANDLE_COUNT=3,
         MAX_STOP_LOSS=0.02,
         TIME_INTERVAL="15 mins",
         HISTORY_DATA_INTERVAL="1 D",
         TAKE_PROFIT_RATIO=1.5):
    if isLong(POSITION_TYPE) or isShort(POSITION_TYPE):
        ib = IB()
        ib.connect(credentials.IB_HOST, credentials.IB_PORT,
                   clientId=credentials.IB_CLIENT_ID)
        contract = Forex(PAIR)

        bars = getHistoricalData(ib, contract)
        marketPrice = getAskPrice(ib, contract)

        if isLong(POSITION_TYPE):
            stopLoss = getCandlesLow(bars[-STOP_LOSS_CANDLE_COUNT:])
            takeProfit = round((marketPrice-stopLoss) *
                               TAKE_PROFIT_RATIO+marketPrice, 5)

        if isShort(POSITION_TYPE):
            stopLoss = getCandlesHigh(bars[-STOP_LOSS_CANDLE_COUNT:])
            takeProfit = round(marketPrice-(stopLoss-marketPrice)
                               * TAKE_PROFIT_RATIO, 5)

        sendMessage(connection, stopLoss, takeProfit,
                    marketPrice, POSITION_TYPE, PAIR)
