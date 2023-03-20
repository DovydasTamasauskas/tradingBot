
import broker.getters as getters
import broker.setters as setters
import shared.log as log
import shared.consts as consts
import notification.notify as notify
from datetime import datetime


def sendMessage(connection, stopLoss, takeProfit, entry, params):
    position = getters.getPosition(params)
    pair = getters.getPair(params)
    maxStopLoss = getters.getMaxStopLoss(params)
    params = setters.setTakeProfit(params, takeProfit)
    params = setters.setEnterPrice(params, entry)
    params = setters.setStopLoss(params, stopLoss)
    enterTime = datetime.now().strftime("%H:%M:%S")
    params = setters.setEnterTime(params, enterTime)

    if maxStopLoss > abs(stopLoss - entry):
        message = str(params)
        title = getSuccessPositionTitle(position, pair)
        log.info(title)
        log.info(message)
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
