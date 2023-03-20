
import shared.log as log
import shared.consts as consts

crypto = 'crypto'
fiat = 'fiat'


contractList = {
    'BTC': crypto,
    'EURUSD': fiat
}


def getMarket(contract):
    try:
        return contractList[contract]
    except:
        log.error(consts.FAILED_TO_GET_CONTRACT_TYPE)
