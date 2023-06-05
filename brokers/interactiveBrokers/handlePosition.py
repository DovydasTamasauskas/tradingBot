import brokers.interactiveBrokers.api as api
import handlers.jsonHandler.getters as getters
import handlers.jsonHandler.setters as setters
import handlers.riskManagmentHandler as riskManagmentHandler
import shared.contracts as contracts
import shared.consts as consts
import notification.helpers.sendMessage as notifyHelper
import shared.log as log
import shared.functions as functions


def getContract(p):
    pair = getters.getPair(p)

    match contracts.getMarket(pair):
        case contracts.crypto:
            contract = api.setCryptoContract(pair)
        case contracts.fiat:
            contract = api.setForexContract(pair)
        case contracts.stock:
            contract = api.setStockContract(pair)
        case _:
            log.error(consts.FAILED_TO_GET_CONTRACT_TYPE)
            return None

    return contract


def getStopLossByCandles(ib, p):
    historicalDataInterval = getters.getHistoryDataInterval(p)
    time = getters.getTime(p)
    contract = getContract(p)

    historicalData = api.getHistoricalData(
        ib, contract, time, historicalDataInterval)
    stopLoss = getStopLossHistorical(
        historicalData, p)

    return stopLoss


def getStopLossHistorical(historicalData, params):
    position = getters.getPosition(params)
    stopLossCanldes = getters.getStopLossCanldes(params)
    historicalData = functions.slice(historicalData, -stopLossCanldes)

    match position:
        case consts.LONG:
            stopLoss = getCandlesLow(historicalData)
        case consts.SHORT:
            stopLoss = getCandlesHigh(historicalData)
        case _:
            log.warrning(consts.FAILED_TO_SET_STOP_LOSS_HISTORICAL)
            return 0

    return round(stopLoss, 5)


def getCandlesLow(array):
    try:
        low = 100000
        for x in array:
            if low > x['low']:
                low = x['low']
        return low
    except:
        log.warrning(consts.FAILED_TO_CALCULATE_LOW)


def getCandlesHigh(array):
    try:
        high = 0
        for x in array:
            if high < x['high']:
                high = x['high']
        return high
    except:
        log.warrning(consts.FAILED_TO_CALCULATE_HIGH)


def handlePosition(p):
    ib = api.openIbConnection()

    marketPrice = api.getMarketPrice(ib, p)

    stopLossByCandles = getStopLossByCandles(ib, p)
    stopLoss = riskManagmentHandler.getStopLoss(
        p, stopLossByCandles, marketPrice)

    takeProfit = riskManagmentHandler.getTakeProfit(p, marketPrice, stopLoss)

    api.createOrder(p)
    api.disconnect(ib)

    return {**p, **{'enterTime': functions.getTimeNow(),
                    'enteryPrice': marketPrice,
                    'stopLoss': stopLoss,
                    'takeProfit': takeProfit,
                    }}
