import broker.interactiveBrokers as interactiveBrokers
import broker.getters as getters
import handlers.riskManagmentHandler as riskManagmentHandler
import handlers.massageHandler as massageHandler
import broker.contracts as contracts
import shared.consts as consts


def handlePosition(connection, p):
    ib = interactiveBrokers.openIbConnection()

    pair = getters.getPair(p)

    match contracts.getMarket(pair):
        case contracts.crypto:
            contract = interactiveBrokers.setCryptoContract(pair)
        case contracts.fiat:
            contract = interactiveBrokers.setForexContract(pair)
        case contracts.stock:
            contract = interactiveBrokers.setStockContract(pair)
        case _:
            print(consts.FAILED_TO_GET_CONTRACT_TYPE)

    marketPrice = interactiveBrokers.getAskPrice(ib, contract)

    stopLoss = riskManagmentHandler.getStopLoss(ib, contract, p)
    takeProfit = riskManagmentHandler.getTakeProfit(stopLoss, marketPrice, p)

    massageHandler.sendMessage(connection, stopLoss, takeProfit,
                               marketPrice, contract, p)
