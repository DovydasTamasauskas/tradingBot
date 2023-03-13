
import shared.consts as consts
import shared.print as print
import ib_insync
import credentials


def openIbConnection():
    try:
        ib = ib_insync.IB()
        ib.connect(credentials.IB_HOST, credentials.IB_PORT,
                   clientId=credentials.IB_CLIENT_ID)
        return ib
    except:
        print.error(consts.FAILED_TO_LOGIN_INTO_BROKER_ACCOUNT)


def getAskPrice(ib: ib_insync, contract: ib_insync.Forex):
    try:
        market = ib.reqMktData(contract, '', False, False)
        ib.sleep(2)
        return market.ask
    except:
        print.warrning(consts.FAILED_TO_FETCH_MARKET_DATA)
        return None


def getHistoricalData(ib: ib_insync, contract: ib_insync.Forex, timeInterval: int, historyInterval: int):
    try:
        return ib.reqHistoricalData(
            contract, endDateTime='', durationStr=historyInterval,
            barSizeSetting=timeInterval, whatToShow='MIDPOINT', useRTH=True)
    except:
        print.warrning(consts.FAILED_TO_FETCH_HISTORICAL_DATA)
        return None


def setContract(pair: str):
    return ib_insync.Forex(pair)
