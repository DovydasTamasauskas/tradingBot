import credentials
import send
import ib_insync


def getCandlesLow(array):
    return min(list(map(lambda x: x.low, array)))


def getCandlesHigh(array):
    return max(list(map(lambda x: x.high, array)))


def getAskPrice(ib, contract):
    market = ib.reqMktData(contract, '', False, False)
    ib.sleep(2)
    return market.ask


def getHistoricalData(ib, contract, timeInterval, historyInterval):
    return ib.reqHistoricalData(
        contract, endDateTime='', durationStr=historyInterval,
        barSizeSetting=timeInterval, whatToShow='MIDPOINT', useRTH=True)


def sendMessage(connection, stopLoss, takeProfit, entry, positionType, pair, maxStopLoss):
    if maxStopLoss > abs(stopLoss - entry):
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
HISTORY_DATA_INTERVAL = "1 D"
# add to stopLoss??
# ----------------------------


position = 'position'
pair = 'pair'
time = 'time'
stopLossCanldes = 'stopLossCanldes'
maxStopLoss = 'maxStopLoss'
takeProfitRatio = 'takeProfitRatio'
historyDataInterval = 'historyDataInterval'


def main(connection, params):
    if isLong(params[position]) or isShort(params[position]):
        ib = ib_insync.IB()
        ib.connect(credentials.IB_HOST, credentials.IB_PORT,
                   clientId=credentials.IB_CLIENT_ID)
        contract = ib_insync.Forex(params[pair])

        bars = getHistoricalData(
            ib, contract, params[time], params[historyDataInterval])
        marketPrice = getAskPrice(ib, contract)

        if isLong(params[position]):
            stopLoss = getCandlesLow(bars[-params[stopLossCanldes]:])
            takeProfit = round((marketPrice-stopLoss) *
                               params[takeProfitRatio]+marketPrice, 5)

        if isShort(params[position]):
            stopLoss = getCandlesHigh(bars[-params[stopLossCanldes]:])
            takeProfit = round(marketPrice-(stopLoss-marketPrice)
                               * params[takeProfitRatio], 5)

        sendMessage(connection, stopLoss, takeProfit,
                    marketPrice, params[position], params[pair], params[maxStopLoss])
