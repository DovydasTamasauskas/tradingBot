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


def sendMessage(connection, stopLoss, takeProfit, contract, params):
    position = getters.getPosition(params)
    pair = getters.getPair(params)
    maxStopLoss = getters.getMaxStopLoss(params)
    marketPrice = getters.getMarketPrice(params)

    params = setters.setTakeProfit(params, takeProfit)
    params = setters.setStopLoss(params, stopLoss)
    enterTime = datetime.now().strftime("%H:%M:%S")
    params = setters.setEnterTime(params, enterTime)

    if maxStopLoss > abs(stopLoss - marketPrice):
        message = str(params)
        title = getSuccessPositionTitle(position, pair)
        api.createOrder(contract, params)
    else:
        message = str(params)
        title = getFailedPositionTitle(position, pair)
        log.info(consts.EXCEEDED_STOPLOSS_LIMIT)
    notify.sendMail(connection, title, message)


def getPositionTitle(positionType: str, pair):
    return positionType + " " + pair


def getSuccessPositionTitle(positionType: str, pair):
    return "Entered " + getPositionTitle(positionType, pair)


def getFailedPositionTitle(positionType: str, pair):
    return "Failed to enter " + getPositionTitle(positionType, pair)


def handlePosition(connection, p):
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

    marketPrice = api.getAskPrice(ib, contract)
    p = setters.setMarketPrice(p, marketPrice)

    limitPrice = getters.getLimitPrice(p)

    entryPrice = marketPrice
    if limitPrice > 0:
        entryPrice = limitPrice

    p = setters.setEnteryPrice(p, entryPrice)

    historicalData = getHistoricalData(ib, contract, p)

    stopLoss = riskManagmentHandler.getStopLoss(historicalData, p)
    p = setters.setStopLoss(p, stopLoss)
    takeProfit = riskManagmentHandler.getTakeProfit(p)

    sendMessage(connection, stopLoss, takeProfit,
                contract, p)
