
import shared.consts as consts
import shared.log as log
import ib_insync
import credentials
import broker.getters as getters


def openIbConnection():
    try:
        ib = ib_insync.IB()
        ib.connect(credentials.IB_HOST, credentials.IB_PORT,
                   clientId=credentials.IB_CLIENT_ID)
        return ib
    except:
        log.error(consts.FAILED_TO_LOGIN_INTO_BROKER_ACCOUNT)


def getAskPrice(ib, contract):
    try:
        market = ib.reqMktData(contract, '', False, False)
        ib.sleep(2)
        return market.ask
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
        return historicalData
    except:
        log.error(consts.FAILED_TO_FETCH_HISTORICAL_DATA)
        return None


def createOrder(contract, params):
    position = getters.getPosition(params)
    size = getters.getSize(params)
    if position == 'long':
        position2 = "BUY"
    if position == "short":
        position2 = "SELL"
    log.info("entered position "+position2 + " "+str(size))
    log.info(str(params))
    # ib = ib_insync.IB()
    # order = ib_insync.LimitOrder(position2, size, 1.11)
    # trade = ib.placeOrder(contract, order)
    # print(trade)


def setForexContract(pair):
    return ib_insync.Forex(pair)


def setCryptoContract(pair):
    return ib_insync.Crypto(pair, 'PAXOS', 'USD')


def setStockContract(stock):
    return ib_insync.Stock(stock, 'SMART', 'USD')
    # return ib_insync.Stock(stock, 'N.VILNIUS', 'EUR')
