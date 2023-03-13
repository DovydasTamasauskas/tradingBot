import broker.interactiveBrokers as interactiveBrokers
import broker.getters as getters
import riskManagment
import massageHandler


def handlePosition(connection, p):
    ib = interactiveBrokers.openIbConnection()

    pair = getters.getPair(p)
    contract = interactiveBrokers.setContract(pair)

    marketPrice = interactiveBrokers.getAskPrice(ib, contract)

    stopLoss = riskManagment.getStopLoss(ib, contract, p)
    takeProfit = riskManagment.getTakeProfit(stopLoss, marketPrice, p)

    massageHandler.sendMessage(connection, stopLoss, takeProfit,
                               marketPrice, p)
