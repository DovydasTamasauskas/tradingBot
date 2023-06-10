import brokers.kraken.api as api
import time
import handlers.jsonHandler.getters as getters
import handlers.riskManagmentHandler as riskManagmentHandler
import shared.consts as consts
import shared.log as log
import shared.functions as functions


DEFAULT_PAIR = 'XXBTZUSD'
DEFAULT_VOLUME = 0.0001


def openPosition(pair, type, ordertype, price=None, volume=DEFAULT_VOLUME, leverage='none'):
    api.sendPrivateRequest('AddOrder', pair, type,
                           volume, leverage, ordertype, price)


def getHistoricalTicks(pair, interval, candlesRange):
    if interval == '15 mins':  # TODO fix bug in interactive brkers
        interval = 15
    else:
        interval = 15
    nowts = int(round(time.time()))
    since = nowts - interval*60*candlesRange
    return api.sendPublicRequest('OHLC', pair,  interval, since)[pair]


def getMarketPrice(p, pair):
    if getters.getEnteryPriceNO_ERROR(p) == 0:  # for test only
        ticker = api.sendPublicRequest('Ticker', pair)[pair]

        # documentation - https://docs.kraken.com/rest/#tag/Market-Data/operation/getTickerInformation
        return float(ticker['c'][0])
    else:
        return getters.getEnteryPriceNO_ERROR(p)


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
    ohlc = getHistoricalTicks(pair, interval, candlesRange)
    lows = []
    for tick in ohlc:
        lows.append(float(tick[3]))
    return sorted(lows)[0]


def getCandlesHight(pair, interval, candlesRange):
    ohlc = getHistoricalTicks(pair, interval, candlesRange)
    highs = []
    for tick in ohlc:
        highs.append(float(tick[2]))
    return sorted(highs, reverse=True)[0]


def getStopLossByCandles(p):
    position = getters.getPosition(p)
    interval = getters.getTime(p)
    stopLossCanldes = getters.getStopLossCanldes(p)

    match position:
        case consts.LONG:
            stopLoss = getCandlesLow(DEFAULT_PAIR, interval, stopLossCanldes)
        case consts.SHORT:
            stopLoss = getCandlesHight(DEFAULT_PAIR, interval, stopLossCanldes)
        case _:
            log.warrning(consts.FAILED_TO_SET_STOP_LOSS_PERCENT)
            return 0

    return stopLoss


def open(p, stopLoss, takeProfit):
    if (getters.getPosition(p) == consts.SHORT):
        openPosition(DEFAULT_PAIR, 'buy', 'limit', round(takeProfit, 1))
        openPosition(DEFAULT_PAIR, 'buy', 'stop-loss', round(stopLoss, 1))
        # openPosition(DEFAULT_PAIR, 'sell', 'market')
    else:
        openPosition(DEFAULT_PAIR, 'sell', 'limit', round(takeProfit, 1))
        openPosition(DEFAULT_PAIR, 'sell', 'stop-loss', round(stopLoss, 1))
        # openPosition(DEFAULT_PAIR, 'buy', 'market')

    # TODO move porition printing to shared file
    logEnteredPosition = getters.getLogEnteredPosition(p)
    if logEnteredPosition == True:
        log.info("entered position " + getters.getPosition(p))
        log.info("limit - " + str(takeProfit))
        log.info("stopLoss - " + str(stopLoss))


def handlePosition(p):
    marketPrice = getMarketPrice(p, DEFAULT_PAIR)

    stopLossByCandles = getStopLossByCandles(p)

    stopLoss = riskManagmentHandler.getStopLoss(
        p, stopLossByCandles, marketPrice)

    takeProfit = riskManagmentHandler.getTakeProfit(p, marketPrice, stopLoss)

    open(p, stopLoss, takeProfit)

    return {**p, **{'enterTime': functions.getTimeNow(),
                    'enteryPrice': marketPrice,
                    'stopLoss': stopLoss,
                    'takeProfit': takeProfit,
                    }}
