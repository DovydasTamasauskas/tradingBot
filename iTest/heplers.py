import sys
import shared.consts as consts
import shared.log as log


def isTest():
    arg = sys.argv
    if len(arg) > 1:
        return sys.argv[1] == consts.TEST
    return False


def isSendEmail():
    arg = sys.argv
    if len(arg) > 1:
        return sys.argv[1] == consts.SEND_EMAIL
    return False


def testTitle(title):
    print('- ' * 20)
    log.info(consts.TEST_RUNNING_MESSAGE)
    log.info(title)


def createJson(position="long", pair="EURUSD", size=100, time="15 mins",
               stopLossCanldes=3, maxStopLoss=100, takeProfitRatio=1.5, historyDataInterval="1 D", alertPrice=1.5,
               alertTime="10:10:10", limitPrice=100.0, stopLossPercent=2, sendResultEmail=False, logEnteredPosition=False):
    return {
        "position": position,
        "pair": pair,
        "size": size,
        "time": time,
        "stopLossCanldes": stopLossCanldes,
        "maxStopLoss": maxStopLoss,
        "takeProfitRatio": takeProfitRatio,
        "historyDataInterval": historyDataInterval,
        "alertPrice": alertPrice,
        "alertTime": alertTime,
        "limitPrice": limitPrice,
        "stopLossPercent": stopLossPercent,
        "sendResultEmail": sendResultEmail,
        "logEnteredPosition": logEnteredPosition
    }


def createJson2(position="long",
                pair="EURUSD", size=100, time="15 mins", stopLossCanldes=None, maxStopLoss=None, takeProfitRatio=None,
                limitPrice=None, stopLossPercent=None):
    results = {
        "position": position,
        "pair": pair,
        "size": size,
        "time": time,
        "sendResultEmail": False,
        "logEnteredPosition": False
    }

    if stopLossCanldes != None and stopLossCanldes > 0:
        results = {**results, **{"stopLossCanldes": stopLossCanldes}}

    if maxStopLoss != None and maxStopLoss > 0:
        results = {**results, **{"maxStopLoss": maxStopLoss}}

    if takeProfitRatio != None and takeProfitRatio > 0:
        results = {**results, **{"takeProfitRatio": takeProfitRatio}}

    if limitPrice != None and limitPrice > 0:
        results = {**results, **{"limitPrice": limitPrice}}

    if stopLossPercent != None and stopLossPercent > 0:
        results = {**results, **{"stopLossPercent": stopLossPercent}}

    return results
