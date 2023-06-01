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


def getStopLoss(ib, p):
    contract = getContract(p)
    realStopLossCanldes = getters.getRealStopLossCanldes(p)

    if realStopLossCanldes == 0:
        stopLoss = riskManagmentHandler.getStopLossPercent(p)
    else:
        historicalDataInterval = getters.getHistoryDataInterval(p)
        time = getters.getTime(p)

        historicalData = api.getHistoricalData(
            ib, contract, time, historicalDataInterval)
        stopLoss = riskManagmentHandler.getStopLossHistorical(
            historicalData, p)

    return stopLoss


def handlePosition(p):
    p = functions.setEnterTimeNow(p)

    ib = api.openIbConnection()

    marketPrice = api.getMarketPrice(ib, p)
    p = functions.setEntryPrice(p, marketPrice)

    stopLoss = getStopLoss(ib, p)
    p = setters.setStopLoss(p, stopLoss)

    takeProfit = riskManagmentHandler.getTakeProfit(p)
    p = setters.setTakeProfit(p, takeProfit)

    notifyHelper.sendMessage(p)
    api.createOrder(p)
    api.disconnect(ib)

    return p
