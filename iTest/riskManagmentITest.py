import shared.log as log
import notification.gmail as notification
import brokers.interactiveBrokers.handlePosition as interactiveBrokers
import handlers.jsonHandler.getters as getters
import iTest.heplers as heplers


def stopLossITest():
    heplers.testTitle("stopLoss should be calculated correctly")
    resultJSON = interactiveBrokers.handlePosition({
        "position": "long",
        "pair": "EURUSD",
        "size": 100,
        "time": "15 mins",
        "stopLossPercent": 2,
        "maxStopLoss": 2,
        "limitPrice": 100,
        "sendResultEmail": False,
        "logEnteredPosition": False
    })

    stopLoss = getters.getStopLoss(resultJSON)
    if stopLoss == 98:
        log.success("test passed")
    else:
        log.error("test failed. Got:" + str(stopLoss) + " Expected: 98")


def takeProfitITest():
    heplers.testTitle("takeProfit should be calculated correctly")
    resultJSON = interactiveBrokers.handlePosition({
        "position": "long",
        "pair": "EURUSD",
        "size": 100,
        "time": "15 mins",
        "stopLossPercent": 2,
        "maxStopLoss": 2,
        "limitPrice": 100,
        "sendResultEmail": False,
        "logEnteredPosition": False
    })

    takeProfit = getters.getTakeProfit(resultJSON)
    if takeProfit == 103:
        log.success("test passed")
    else:
        log.error("test failed. Got:" + str(takeProfit) + " Expected: 103")


def runTests():
    stopLossITest()
    takeProfitITest()
