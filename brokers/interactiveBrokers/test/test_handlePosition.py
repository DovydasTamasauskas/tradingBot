import unittest
import brokers.interactiveBrokers.handlePosition as handlePosition
import shared.log as log
from unittest.mock import MagicMock
import brokers.interactiveBrokers.api as api
import handlers.riskManagmentHandler as riskManagmentHandler
import notification.helpers.messages as notifyHelper
import shared.functions as functions


class TestHandlePositionFunction(unittest.TestCase):

    def setUp(self) -> None:
        log.PRINT_ERRORS = False

    def test_handlePosition(self):

        api.openIbConnection = MagicMock()
        api.openIbConnection.return_value = ''

        api.getMarketPrice = MagicMock()
        api.getMarketPrice.return_value = 100

        handlePosition.getStopLossByCandles = MagicMock()
        handlePosition.getStopLossByCandles.return_value = 99

        riskManagmentHandler.getStopLoss = MagicMock()
        riskManagmentHandler.getStopLoss.return_value = 99

        riskManagmentHandler.getTakeProfit = MagicMock()
        riskManagmentHandler.getTakeProfit.return_value = 102

        notifyHelper.sendEmail = MagicMock()

        api.createOrder = MagicMock()

        api.disconnect = MagicMock()

        functions.getTimeNow = MagicMock()
        functions.getTimeNow.return_value = '10:10:10'

        results = handlePosition.handlePosition({})

        self.assertEqual(results, {'enterTime': '10:10:10', 'enteryPrice': 100,
                                   'stopLoss': 99, 'takeProfit': 102})


if __name__ == '__main__':
    unittest.main()
