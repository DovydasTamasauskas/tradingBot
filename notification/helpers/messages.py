import brokers.interactiveBrokers.api as api
import handlers.jsonHandler.getters as getters
import shared.consts as consts
import notification.gmail as gmail
import shared.log as log


def getPositionTitle(positionType: str, pair):
    return positionType + " " + pair


def getSuccessPositionTitle(positionType: str, pair):
    return consts.RESULTS + ": Entered " + getPositionTitle(positionType, pair)


def getFailedPositionTitle(positionType: str, pair):
    return consts.RESULTS + ": Failed to enter " + getPositionTitle(positionType, pair)


def sendEmail(params):
    sendResult = getters.getSendResultEmail(params)
    if sendResult == True:
        position = getters.getPosition(params)
        pair = getters.getPair(params)
        title = getSuccessPositionTitle(position, pair)
        gmail.sendMail(title, consts.RESULTS+str(params))


def printToConsole(p):
    logEnteredPosition = getters.getLogEnteredPosition(p)
    if logEnteredPosition == True:
        log.info("entered position - " + getters.getPosition(p))
        log.info("entered price - " + str(getters.getEnteryPrice(p)))
        log.info("limit - " + str(getters.getTakeProfit(p)))
        log.info("stopLoss - " + str(getters.getStopLoss(p)))
