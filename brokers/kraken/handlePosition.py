import brokers.kraken.api as api

DEFAULT_PAIR = 'XBTUSD'
DEFAULT_VOLUME = 0.0001


def openPosition(pair, type, ordertype, price, volume=DEFAULT_VOLUME, leverage='none'):
    api.sendPrivateRequest('AddOrder', pair, type,
                           volume, leverage, ordertype, price)


def getBalance():
    api.sendPrivateRequest('Balance')


def main():
    openPosition(DEFAULT_PAIR, 'buy', 'limit', '26600')
    openPosition(DEFAULT_PAIR, 'buy', 'stop-loss', '30000')
    getBalance()
