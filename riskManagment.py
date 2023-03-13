
import shared.functions as functions
import broker.interactiveBrokers as interactiveBrokers
import broker.getters as getters


def getStopLoss(ib, contract, params):

    stopLossCanldes = getters.getStopLossCanldes(params)
    time = getters.getTime(params)
    historicalDataInterval = getters.getHistoryDataInterval(params)

    historicalData = interactiveBrokers.getHistoricalData(
        ib, contract, time, historicalDataInterval)
    stopLossCandles = functions.slice(historicalData, -stopLossCanldes)
    stopLoss = getCandlesLow(stopLossCandles)
    print(stopLoss)
    return stopLoss


def getTakeProfit():
    return 0.06


def getCandlesLow(array):
    return min(list(map(lambda x: x.low, array)))


def getCandlesHigh(array):
    return max(list(map(lambda x: x.high, array)))
