import brokers.interactiveBrokers.api as api
import handlers.jsonHandler.getters as getters
import handlers.jsonHandler.setters as setters
import handlers.riskManagmentHandler as riskManagmentHandler
import shared.contracts as contracts
import shared.consts as consts
import notification.notify as notify
from datetime import datetime
import shared.log as log


def getHistoricalData(ib, contract, p):
    historicalDataInterval = getters.getHistoryDataInterval(p)
    time = getters.getTime(p)

    return api.getHistoricalData(
        ib, contract, time, historicalDataInterval)


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


def handlePosition(p):
    timeNow = datetime.now().strftime("%H:%M:%S")
    log.info(consts.MESSAGE_FOUND + " " + timeNow)
    ib = api.openIbConnection()

    contract = getContract(p)

    limitPrice = getters.getLimitPrice(p)

    entryPrice = 0
    if limitPrice > 0:
        entryPrice = limitPrice
    else:
        marketPrice = api.getAskPrice(ib, contract)
        entryPrice = marketPrice
        p = setters.setMarketPrice(p, marketPrice)

    p = setters.setEnteryPrice(p, entryPrice)

    stopLossPercent = getters.getStopLossPercent(p)
    stopLoss = 0
    if stopLossPercent > 0:
        p = setters.setStopLossPercent(p, stopLossPercent)
        stopLoss = riskManagmentHandler.getStopLossPercent(p)
    else:
        historicalData = getHistoricalData(ib, contract, p)
        stopLoss = riskManagmentHandler.getStopLossHistorical(
            historicalData, p)

    p = setters.setStopLoss(p, stopLoss)
    takeProfit = riskManagmentHandler.getTakeProfit(p)
    p = setters.setTakeProfit(p, takeProfit)

    p = setters.setEnterTime(p, timeNow)

    sendMessage(contract, p)

    api.disconnect(ib)

    return p
