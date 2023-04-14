import shared.log as log
import notification.gmail as notification
import brokers.interactiveBrokers.handlePosition as interactiveBrokers
import handlers.jsonHandler.getters as getters
import iTest.heplers as heplers


def riskManagmentITest1():
    heplers.testTitle("limit order long should be calculated correctly")

    TEST_JSON = heplers.createJson(
        stopLossPercent=2, maxStopLoss=2, limitPrice=100)
    results = interactiveBrokers.handlePosition(TEST_JSON)

    stopLoss = getters.getStopLoss(results)
    takeProfit = getters.getTakeProfit(results)

    if stopLoss == 98 and takeProfit == 103:
        log.success("test passed")
    else:
        log.error("test failed. Got:" + str(stopLoss) + " Expected: 98")


def riskManagmentITest2():
    heplers.testTitle("limit short long should be calculated correctly")

    TEST_JSON = heplers.createJson(
        position="short", stopLossPercent=2, maxStopLoss=2, limitPrice=100)
    results = interactiveBrokers.handlePosition(TEST_JSON)

    stopLoss = getters.getStopLoss(results)
    takeProfit = getters.getTakeProfit(results)

    if stopLoss == 102 and takeProfit == 97:
        log.success("test passed")
    else:
        log.error("test failed. Got:" + str(stopLoss) + " Expected: 102")


def riskManagmentITest3():
    heplers.testTitle(
        "maxStopLossPercent should override stopLossPercent long position")

    TEST_JSON = heplers.createJson(stopLossPercent=2)
    results = interactiveBrokers.handlePosition(TEST_JSON)

    enterPrice = getters.getEnteryPrice(results)
    stopLoss = getters.getStopLoss(results)
    takeProfit = getters.getTakeProfit(results)

    if round(stopLoss*100/enterPrice, 1) == 99 and round(takeProfit*100/enterPrice, 1) == 101.5:
        log.success("test passed")
        return 0

    log.error("test failed")


def riskManagmentITest4():
    heplers.testTitle(
        "maxStopLossPercent should override stopLossPercent short position")

    TEST_JSON = heplers.createJson(position="short", stopLossPercent=2)
    results = interactiveBrokers.handlePosition(TEST_JSON)

    enterPrice = getters.getEnteryPrice(results)
    stopLoss = getters.getStopLoss(results)
    takeProfit = getters.getTakeProfit(results)

    if round(stopLoss*100/enterPrice, 1) == 101 and round(takeProfit*100/enterPrice, 1) == 98.5:
        log.success("test passed")
        return 0

    log.error("test failed")


def riskManagmentITest5():
    heplers.testTitle("market order stopLoss and takeProfit long position")

    TEST_JSON = heplers.createJson()
    results = interactiveBrokers.handlePosition(TEST_JSON)

    enterPrice = getters.getEnteryPrice(results)
    stopLoss = getters.getStopLoss(results)
    takeProfit = getters.getTakeProfit(results)

    if round(stopLoss*100/enterPrice, 1) == 99 and round(takeProfit*100/enterPrice, 1) == 101.5:
        log.success("test passed")
        return 0

    log.error("test failed")


def riskManagmentITest6():
    heplers.testTitle("market order stopLoss and takeProfit short position")

    TEST_JSON = heplers.createJson(position="short")
    results = interactiveBrokers.handlePosition(TEST_JSON)

    enterPrice = getters.getEnteryPrice(results)
    stopLoss = getters.getStopLoss(results)
    takeProfit = getters.getTakeProfit(results)

    if round(stopLoss*100/enterPrice, 1) == 101 and round(takeProfit*100/enterPrice, 1) == 98.5:
        log.success("test passed")
        return 0

    log.error("test failed")


def riskManagmentITest7():
    heplers.testTitle(
        "profitRatio should override default value long position")

    TEST_JSON = heplers.createJson(takeProfitRatio=3)
    results = interactiveBrokers.handlePosition(TEST_JSON)

    enterPrice = getters.getEnteryPrice(results)
    stopLoss = getters.getStopLoss(results)
    takeProfit = getters.getTakeProfit(results)

    if round(stopLoss*100/enterPrice, 1) == 99 and round(takeProfit*100/enterPrice, 1) == 103:
        log.success("test passed")
        return 0

    log.error("test failed")


def riskManagmentITest8():
    heplers.testTitle(
        "profitRatio should override default value short position")

    TEST_JSON = heplers.createJson(position="short", takeProfitRatio=3)
    results = interactiveBrokers.handlePosition(TEST_JSON)

    enterPrice = getters.getEnteryPrice(results)
    stopLoss = getters.getStopLoss(results)
    takeProfit = getters.getTakeProfit(results)

    if round(stopLoss*100/enterPrice, 1) == 101 and round(takeProfit*100/enterPrice, 1) == 97:
        log.success("test passed")
        return 0

    log.error("test failed")


def runTests():
    riskManagmentITest1()
    riskManagmentITest2()
    riskManagmentITest3()
    riskManagmentITest4()
    riskManagmentITest5()
    riskManagmentITest6()
    riskManagmentITest7()
    riskManagmentITest8()
