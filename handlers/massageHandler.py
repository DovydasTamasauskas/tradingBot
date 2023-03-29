
import handlers.jsonHandler.getters as getters
import handlers.jsonHandler.setters as setters
import shared.log as log
import shared.consts as consts
import notification.notify as notify
from datetime import datetime
import brokers.interactiveBrokers.api as api


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
    notify.sendMessage(connection, title, message)


def getPositionTitle(positionType: str, pair):
    return positionType + " " + pair


def getSuccessPositionTitle(positionType: str, pair):
    return "Entered " + getPositionTitle(positionType, pair)


def getFailedPositionTitle(positionType: str, pair):
    return "Failed to enter " + getPositionTitle(positionType, pair)
