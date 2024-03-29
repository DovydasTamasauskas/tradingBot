
import shared.consts as consts
import shared.log as log
import ib_insync
import credentials
import handlers.jsonHandler.getters as getters
import json
import brokers.interactiveBrokers.handlePosition as handlePosition


def openIbConnection():
    try:
        ib = ib_insync.IB()
        ib.connect(credentials.IB_HOST, credentials.IB_PORT,
                   clientId=credentials.IB_CLIENT_ID)
        return ib
    except:
        log.error(consts.FAILED_TO_LOGIN_INTO_BROKER_ACCOUNT)


def disconnect(ib):
    try:
        ib.disconnect()
    except:
        log.error(consts.FAILED_TO_DISCONNECT_FROM_BROKER)


def getMarketPrice(ib, p):
    try:
        if getters.getEnteryPriceNO_ERROR(p) == 0:  # for test only
            contract = handlePosition.getContract(p)
            market = ib.reqMktData(contract, '', False, False)
            ib.sleep(2)
            return market.ask
        else:
            return getters.getEnteryPriceNO_ERROR(p)
    except:
        log.warrning(consts.FAILED_TO_FETCH_MARKET_DATA)
        return None


def getHistoricalData(ib, contract, timeInterval, historyInterval):
    try:
        historicalData = ib.reqHistoricalData(
            contract, endDateTime='', durationStr=historyInterval,
            barSizeSetting=timeInterval, whatToShow='MIDPOINT', useRTH=True)
        if len(historicalData) == 0:
            log.error(consts.FAILED_TO_FETCH_HISTORICAL_DATA)
        returnArray = []
        for x in historicalData:
            returnArray.append({'low': x.low, 'high': x.high})
        return returnArray
    except:
        log.error(consts.FAILED_TO_FETCH_HISTORICAL_DATA)
        return None


def createOrder(ib, params, stopLoss, takeProfit):
    contract = handlePosition.getContract(params)
    size = getters.getSize(params)

    # if takeProfit > 0 and stopLoss > 0:
    # if (getters.getPosition(params) == consts.SHORT):
    # limit = ib_insync.LimitOrder("BUY", size, takeProfit)
    # stopLoss = ib_insync.StopOrder("SELL", size, takeProfit)
    # market = ib_insync.MarketOrder("SELL", size)
    # trade = ib.placeOrder(contract, limit)
    # trade = ib.placeOrder(contract, stopLoss)
    # trade = ib.placeOrder(contract, market)

    logEnteredPosition = getters.getLogEnteredPosition(params)
    if logEnteredPosition == True:

        json_formatted_str = json.dumps(params, indent=2)
        log.info("entered position long "+str(size))
        log.info(json_formatted_str)


def setForexContract(pair):
    return ib_insync.Forex(pair)


def setCryptoContract(pair):
    return ib_insync.Crypto(pair, 'PAXOS', 'USD')


def setStockContract(stock):
    return ib_insync.Stock(stock, 'SMART', 'USD')
    # return ib_insync.Stock(stock, 'N.VILNIUS', 'EUR')
