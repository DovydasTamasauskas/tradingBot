import brokers.interactiveBrokers.api as api
import handlers.jsonHandler.getters as getters
import handlers.jsonHandler.setters as setters
import handlers.riskManagmentHandler as riskManagmentHandler
import handlers.massageHandler as massageHandler
import shared.contracts as contracts
import shared.consts as consts


def handlePosition(connection, p):
    ib = api.openIbConnection()

    pair = getters.getPair(p)

    match contracts.getMarket(pair):
        case contracts.crypto:
            contract = api.setCryptoContract(pair)
        case contracts.fiat:
            contract = api.setForexContract(pair)
        case contracts.stock:
            contract = api.setStockContract(pair)
        case _:
            print(consts.FAILED_TO_GET_CONTRACT_TYPE)

    marketPrice = api.getAskPrice(ib, contract)
    p = setters.setMarketPrice(p, marketPrice)

    stopLoss = riskManagmentHandler.getStopLoss(ib, contract, p)
    p = setters.setStopLoss(p, stopLoss)
    takeProfit = riskManagmentHandler.getTakeProfit(p)

    massageHandler.sendMessage(connection, stopLoss, takeProfit,
                               contract, p)
