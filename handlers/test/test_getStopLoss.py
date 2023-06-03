import unittest
import brokers.interactiveBrokers.handlePosition as handlePosition
import shared.log as log
from unittest.mock import MagicMock
import brokers.interactiveBrokers.api as api
import handlers.riskManagmentHandler as riskManagmentHandler


class TestGetStopLossFunction(unittest.TestCase):

    def setUp(self) -> None:
        log.PRINT_ERRORS = False

    def test_GetStopLoss(self):

        riskManagmentHandler.getMaxStopLossByPercent = MagicMock()
        riskManagmentHandler.getMaxStopLossByPercent.return_value = 10

        results = handlePosition.getStopLoss({}, 5)
        self.assertEqual(results, 10)

    def test_GetStopLoss2(self):

        riskManagmentHandler.isStopLossExceeded = MagicMock()
        riskManagmentHandler.isStopLossExceeded.return_value = False

        results = handlePosition.getStopLoss({'stopLossCanldes': 2}, 5)
        self.assertEqual(results, 5)

    def test_GetStopLoss3(self):

        riskManagmentHandler.isStopLossExceeded = MagicMock()
        riskManagmentHandler.isStopLossExceeded.return_value = True

        riskManagmentHandler.getMaxStopLossByPercent = MagicMock()
        riskManagmentHandler.getMaxStopLossByPercent.return_value = 10

        results = handlePosition.getStopLoss({'stopLossCanldes': 2}, 5)
        self.assertEqual(results, 10)


if __name__ == '__main__':
    unittest.main()
