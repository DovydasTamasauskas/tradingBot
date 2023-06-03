import unittest
import brokers.interactiveBrokers.handlePosition as handlePosition
import shared.log as log
from unittest.mock import MagicMock
import brokers.interactiveBrokers.api as api
import handlers.riskManagmentHandler as riskManagmentHandler


class TestGetStopLossFunction(unittest.TestCase):

    def setUp(self) -> None:
        log.PRINT_ERRORS = False

    def test_StopLossHistorical(self):
        api.getHistoricalData = MagicMock()
        api.getHistoricalData.return_value = [{'high': 99}, {'high': 99.5}, {
            'high': 101}, {'high': 200}, {'high': 111}, {'high': 222}]

        riskManagmentHandler.getStopLossHistorical = MagicMock()
        riskManagmentHandler.getStopLossHistorical.return_value = 10

        results = handlePosition.getStopLoss('', {"stopLossCanldes": 4})
        self.assertEqual(results, 10)

    def test_StopLossPercent(self):

        riskManagmentHandler.getMaxStopLossByPercent = MagicMock()
        riskManagmentHandler.getMaxStopLossByPercent.return_value = 10

        results = handlePosition.getStopLoss('', {})
        self.assertEqual(results, 10)


if __name__ == '__main__':
    unittest.main()
