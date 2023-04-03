import brokers.interactiveBrokers.api as api
import handlers.jsonHandler.getters as getters
import handlers.jsonHandler.setters as setters
import handlers.riskManagmentHandler as riskManagmentHandler
import shared.contracts as contracts
import shared.consts as consts
import shared.functions as functions
import notification.notify as notify
from datetime import datetime
import shared.log as log


def getHistoricalData(ib, contract, p):
    historicalDataInterval = getters.getHistoryDataInterval(p)

    stopLossCanldes = getters.getStopLossCanldes(p)
    time = getters.getTime(p)
    historicalData = api.getHistoricalData(
        ib, contract, time, historicalDataInterval)
    historicalData = functions.slice(historicalData, -stopLossCanldes)
    return historicalData


def sendMessage(contract, params):
    position = getters.getPosition(params)
    pair = getters.getPair(params)
    maxStopLoss = getters.getMaxStopLoss(params)
    stopLoss = getters.getStopLoss(params)
    entryPrice = getters.getEnteryPrice(params)

    if maxStopLoss < abs(stopLoss - entryPrice):
        title = getFailedPositionTitle(position, pair)
        log.info(consts.EXCEEDED_STOPLOSS_LIMIT)
    else:
        title = getSuccessPositionTitle(position, pair)
        api.createOrder(contract, params)

    sendResult = getters.getSendResultEmail(params)
    if sendResult == True:
        notify.sendMail(title, consts.RESULTS+str(params))


def getPositionTitle(positionType: str, pair):
    return positionType + " " + pair


def getSuccessPositionTitle(positionType: str, pair):
    return consts.RESULTS + ": Entered " + getPositionTitle(positionType, pair)


def getFailedPositionTitle(positionType: str, pair):
    return consts.RESULTS + ": Failed to enter " + getPositionTitle(positionType, pair)


def handlePosition(p):
    ib = api.openIbConnection()

    pair = getters.getPair(p)

    match contracts.getMarket(pair):
        case contracts.crypto:
            contract = api.setCryptoContract(pair)
        case contracts.fiat:
            contract = api.setForexContract(pair)
        case contracts.stock:
            contract = api.setStockContract(pair)
        case _:
            print(consts.FAILED_TO_GET_CONTRACT_TYPE)

    limitPrice = getters.getLimitPrice(p)

    entryPrice = 0
    if limitPrice > 0:
        entryPrice = limitPrice
    else:
        marketPrice = api.getAskPrice(ib, contract)
        entryPrice = marketPrice
        p = setters.setMarketPrice(p, marketPrice)

    p = setters.setEnteryPrice(p, entryPrice)

    historicalData = getHistoricalData(ib, contract, p)

    stopLoss = riskManagmentHandler.getStopLoss(historicalData, p)
    p = setters.setStopLoss(p, stopLoss)
    takeProfit = riskManagmentHandler.getTakeProfit(p)
    p = setters.setTakeProfit(p, takeProfit)
    p = setters.setStopLoss(p, stopLoss)

    enterTime = datetime.now().strftime("%H:%M:%S")
    p = setters.setEnterTime(p, enterTime)

    sendMessage(contract, p)

    api.disconnect(ib)

    return p
