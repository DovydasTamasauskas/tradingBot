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


def createJson(position="long",
               pair="EURUSD", size=100, time="15 mins", enteryPrice=0, stopLossCanldes=None, maxStopLoss=None, takeProfitRatio=None,
               limitPrice=None, stopLossPercent=None, sendResultEmail=None, logEnteredPosition=None):
    results = {
        "position": position,
        "pair": pair,
        "size": size,
        "time": time
    }

    if enteryPrice != None and enteryPrice > 0:
        results = {**results, **{"enteryPrice": enteryPrice}}

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

    if sendResultEmail != None and sendResultEmail > 0:
        results = {**results, **{"sendResultEmail": sendResultEmail}}
    else:
        results = {**results, **{"sendResultEmail": False}}

    if logEnteredPosition != None and logEnteredPosition > 0:
        results = {**results, **{"logEnteredPosition": logEnteredPosition}}
    else:
        results = {**results, **{"logEnteredPosition": False}}

    return results
