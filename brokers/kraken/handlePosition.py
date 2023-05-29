import brokers.kraken.api as api
import time

DEFAULT_PAIR = 'XXBTZUSD'
DEFAULT_VOLUME = 0.0001


def openPosition(pair, type, ordertype, price=None, volume=DEFAULT_VOLUME, leverage='none'):
    api.sendPrivateRequest('AddOrder', pair, type,
                           volume, leverage, ordertype, price)


def getTicks(pair, interval, candlesRange):
    nowts = int(round(time.time()))
    since = nowts - interval*60*candlesRange
    return api.sendPublicRequest('OHLC', pair,  interval, since)[pair]


def getBalance():
    return api.sendPrivateRequest('Balance')


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


def getCandlesLow(pair, interval, candlesRange):
    ohlc = getTicks(pair, interval, candlesRange)
    lows = []
    for tick in ohlc:
        lows.append(float(tick[3]))
    return sorted(lows)[0]


def getCandlesHight(pair, interval, candlesRange):
    ohlc = getTicks(pair, interval, candlesRange)
    highs = []
    for tick in ohlc:
        highs.append(float(tick[2]))
    return sorted(highs, reverse=True)[0]


def main():
    printBalance()
    print('low   - ', getCandlesLow(DEFAULT_PAIR, 15, 4))
    print('hight - ', getCandlesHight(DEFAULT_PAIR, 15, 4))


def handlePosition(p):
    # TODO handle position
    # openPosition(DEFAULT_PAIR, 'buy', 'limit', '26600')
    # openPosition(DEFAULT_PAIR, 'buy', 'stop-loss', '30000')
    # openPosition(DEFAULT_PAIR, 'sell', 'market')
    return 0
