
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
        return ib.reqHistoricalData(
            contract, endDateTime='', durationStr=historyInterval,
            barSizeSetting=timeInterval, whatToShow='MIDPOINT', useRTH=True)
    except:
        log.warrning(consts.FAILED_TO_FETCH_HISTORICAL_DATA)
        return None


def setForexContract(pair):
    return ib_insync.Forex(pair)


def setCryptoContract(pair):
    return ib_insync.Crypto(pair, 'PAXOS', 'USD')
