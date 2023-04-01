import shared.log as log
import notification.notify as notification
import brokers.interactiveBrokers.handlePosition as interactiveBrokers
import handlers.jsonHandler.getters as getters
import iTest.heplers as heplers


def stopLossITest():
    heplers.testTitle("stopLoss should be calculated correctly")
    resultJSON = interactiveBrokers.handlePosition(heplers.createJson())

    stopLoss = getters.getStopLoss(resultJSON)
    if stopLoss == 98:
        log.success("test passed")
    else:
        log.error("test failed")


def takeProfitITest():
    heplers.testTitle("takeProfit should be calculated correctly")
    resultJSON = interactiveBrokers.handlePosition(heplers.createJson())

    takeProfit = getters.getTakeProfit(resultJSON)
    if takeProfit == 103:
        log.success("test passed")
    else:
        log.error("test failed")


def takeProfitStopLossITest():
    heplers.testTitle("TakeProfit and stopLoss should be calculated correctly")
    resultJSON = interactiveBrokers.handlePosition(heplers.createJson())

    stopLoss = getters.getStopLoss(resultJSON)
    takeProfit = getters.getTakeProfit(resultJSON)
    if stopLoss == 98 and takeProfit == 103:
        log.success("test passed")
    else:
        log.error("test failed")


def runTests():
    stopLossITest()
    takeProfitITest()
    takeProfitStopLossITest()
