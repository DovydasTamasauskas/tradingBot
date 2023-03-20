
import broker.getters as getters
import broker.setters as setters
import shared.consts as consts
import notification.notify as notify
from datetime import datetime


def sendMessage(connection, stopLoss, takeProfit, entry, params):
    position = getters.getPosition(params)
    pair = getters.getPair(params)
    maxStopLoss = getters.getMaxStopLoss(params)

    # if maxStopLoss > abs(stopLoss - entry):
    message = getPositionStructure(stopLoss, takeProfit, entry, params)
    title = getSuccessPositionTitle(position, pair)
    print("send message")
    print(title)
    print(message)
    # else:
    #     message = getPositionStructure(stopLoss, takeProfit, entry, params)
    #     title = getFailedPositionTitle(position, pair)
    #     print("error")
    # notify.sendMessage(connection, title, message)


def getPositionStructure(stopLoss: float, takeProfit: float, entry: float, params):
    params = setters.setTakeProfit(params, takeProfit)
    params = setters.setEnterPrice(params, entry)
    params = setters.setStopLoss(params, stopLoss)

    enterTime = datetime.now().strftime("%H:%M:%S")
    params = setters.setEnterTime(params, enterTime)

    return str(params)
    # return "entry =      " + str(entry) + \
    #     "\n stopLoss =   " + str(stopLoss) + \
    #     "\n takeProfit = " + str(takeProfit) + \
    #     "\n" + str(params)


def getPositionTitle(positionType: str, pair):
    return positionType + " " + pair


def getSuccessPositionTitle(positionType: str, pair):
    return "Entered " + getPositionTitle(positionType, pair)


def getFailedPositionTitle(positionType: str, pair):
    return "Failed to enter " + getPositionTitle(positionType, pair)
