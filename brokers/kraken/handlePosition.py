import brokers.kraken.api as api

DEFAULT_PAIR = 'XBTUSD'
DEFAULT_VOLUME = 0.0001


def openPosition(pair, type, ordertype, price=None, volume=DEFAULT_VOLUME, leverage='none'):
    api.sendPrivateRequest('AddOrder', pair, type,
                           volume, leverage, ordertype, price)


def getBalance():
    return api.sendPrivateRequest('Balance')['result']


def printBalance():
    balancesArray = getBalance()
    balances = []
    for coin in balancesArray:
        if float(balancesArray[coin]) > 0.00001:
            balances.append(
                {"name": coin, "balance": float(balancesArray[coin])})

    balancesSorted = sorted(balances, key=lambda x: x["balance"], reverse=True)

    print('-' * 30)
    print('Balance')
    for coin in balancesSorted:
        print("%(name)s - %(balance)s" % {
            'name': coin['name'], 'balance': coin['balance']})
    print('-' * 30)


def main():
    printBalance()
    # getOHLC()
    # openPosition(DEFAULT_PAIR, 'buy', 'limit', '26600')
    # openPosition(DEFAULT_PAIR, 'buy', 'stop-loss', '30000')
    # openPosition(DEFAULT_PAIR, 'sell', 'market')


def handlePosition(p):
    # TODO handle position
    return 0
