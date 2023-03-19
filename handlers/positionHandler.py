import broker.interactiveBrokers as interactiveBrokers
import broker.getters as getters
import handlers.riskManagmentHandler as riskManagmentHandler
import handlers.massageHandler as massageHandler


def handlePosition(connection, p):
    ib = interactiveBrokers.openIbConnection()

    pair = getters.getPair(p)
    contract = interactiveBrokers.setForexContract(pair)

    marketPrice = interactiveBrokers.getAskPrice(ib, contract)

    stopLoss = riskManagmentHandler.getStopLoss(ib, contract, p)
    takeProfit = riskManagmentHandler.getTakeProfit(stopLoss, marketPrice, p)

    massageHandler.sendMessage(connection, stopLoss, takeProfit,
                               marketPrice, p)
