
import shared.log as log
import shared.consts as consts

crypto = 'crypto'
fiat = 'fiat'
stock = 'stock'


contractList = {
    'BTC': crypto,
    'EURUSD': fiat,
    'TSLA': stock,
    'SAB1L': stock,
}


def getMarket(contract):
    try:
        return contractList[contract]
    except:
        log.error(consts.FAILED_TO_GET_CONTRACT_TYPE)
