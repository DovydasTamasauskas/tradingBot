
import shared.consts as consts
import shared.log as log
import ib_insync
import credentials


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


def createOrder():
    #  ib_insync.order.StopLimitOrder(action='BUY', totalQuantity=1, stopPrice=20000, lmtPrice=30000)
    # ib_insync.order.MarketOrder(action='BUY', totalQuantity=10000)
    ib = ib_insync.IB()
    contract = ib_insync.Forex('EURUSD')
    # ib.qualifyContracts(contract)

    order = ib_insync.LimitOrder('SELL', 20000, 1.11)
    trade = ib.placeOrder(contract, order)
    print(trade)


def setForexContract(pair):
    return ib_insync.Forex(pair)


def setCryptoContract(pair):
    return ib_insync.Crypto(pair, 'PAXOS', 'USD')


def setStockContract(stock):
    return ib_insync.Stock(stock, 'SMART', 'USD')
    # return ib_insync.Stock(stock, 'N.VILNIUS', 'EUR')
