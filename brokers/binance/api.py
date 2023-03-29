
import shared.consts as consts
import shared.log as log
import credentials
import handlers.jsonHandler.getters as getters
from binance.spot import Spot


def openConnection():
    try:
        client = Spot(api_key=credentials.BINANCE_API_KEY,
                      api_secret=credentials.BINANCE_API_SECRET)
        return client
    except:
        log.error(consts.FAILED_TO_LOGIN_INTO_BROKER_ACCOUNT)


def getAskPrice(client, symbol):
    try:
        return client.ticker_price(symbol)
    except:
        log.warrning(consts.FAILED_TO_FETCH_MARKET_DATA)
        return None


def getHistoricalData():
    try:
        return 0
    except:
        log.error(consts.FAILED_TO_FETCH_HISTORICAL_DATA)
        return None


def createOrder(client, props):
    params = {
        'symbol': 'BTCUSDT',
        'side': 'BUY',
        'type': 'LIMIT',
        'timeInForce': 'GTC',
        'quantity': 0.002,
        'price': 9500
    }

    response = client.new_order(**params)
    print(response)
