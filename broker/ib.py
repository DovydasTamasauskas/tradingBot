import credentials
import send
import ib_insync
import sys
from . import getters
from . import defaultProps
from . import messages


def getCandlesLow(array):
    return min(list(map(lambda x: x.low, array)))


def getCandlesHigh(array):
    return max(list(map(lambda x: x.high, array)))


def getAskPrice(ib, contract):
    try:
        market = ib.reqMktData(contract, '', False, False)
        ib.sleep(2)
    except:
        print(messages.FAILED_TO_GET_MARKET_DATA)
        return None
    return market.ask


def getHistoricalData(ib, contract, timeInterval, historyInterval):
    try:
        return ib.reqHistoricalData(
            contract, endDateTime='', durationStr=historyInterval,
            barSizeSetting=timeInterval, whatToShow='MIDPOINT', useRTH=True)
    except:
        print(messages.FAILED_TO_GET_HISTORICAL_DATA)
        return None


def sendMessage(connection, stopLoss, takeProfit, entry, positionType, pair, maxStopLoss):
    if maxStopLoss > abs(stopLoss - entry):
        message = getPositionStructure(stopLoss, takeProfit, entry)
        title = getSuccessPositionTitle(positionType, pair)
    else:
        message = messages.EXEDED_STOPLOSS_LIMIT
        title = getFailedPositionTitle(positionType, pair)
    send.sendMessage(connection, title, message)


def getPositionStructure(stopLoss, takeProfit, entry):
    return "entry =      " + str(entry) + \
        "\n stopLoss =   " + str(stopLoss) + \
        "\n takeProfit = " + str(takeProfit)


def getPositionTitle(positionType, pair):
    return positionType + " " + pair


def getSuccessPositionTitle(positionType, pair):
    return "Entered " + getPositionTitle(positionType, pair)


def getFailedPositionTitle(positionType, pair):
    return "Failed to enter " + getPositionTitle(positionType, pair)


def isLong(param):
    return param.lower() == defaultProps.LONG


def isShort(param):
    return param.lower() == defaultProps.SHORT


def openIbConnection():
    try:
        ib = ib_insync.IB()
        ib.connect(credentials.IB_HOST, credentials.IB_PORT,
                   clientId=credentials.IB_CLIENT_ID)
    except:
        print(messages.FAILED_TO_LOGIN_INTO_BROKER_ACCOUNT)
        sys.exit()
    return ib


def main(connection, p):
    if isLong(getters.getPosition(p)) or isShort(getters.getPosition(p)):
        ib = openIbConnection()
        contract = ib_insync.Forex(getters.getPair(p))

        bars = getHistoricalData(
            ib, contract, getters.getTime(p), getters.getHistoryDataInterval(p))
        marketPrice = getAskPrice(ib, contract)

        if bars != None and marketPrice != None:
            if isLong(getters.getPosition(p)):
                stopLoss = getCandlesLow(bars[-getters.getStopLossCanldes(p):])
                takeProfit = round((marketPrice-stopLoss) *
                                   getters.getTakeProfitRatio(p)+marketPrice, 5)

            if isShort(getters.getPosition(p)):
                stopLoss = getCandlesHigh(
                    bars[-getters.getStopLossCanldes(p):])
                takeProfit = round(marketPrice-(stopLoss-marketPrice)
                                   * getters.getTakeProfitRatio(p), 5)

            sendMessage(connection, stopLoss, takeProfit,
                        marketPrice, getters.getPosition(p), getters.getPair(p), getters.getMaxStopLoss(p))
