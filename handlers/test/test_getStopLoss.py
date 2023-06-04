import unittest
import shared.log as log
from unittest.mock import MagicMock
import handlers.riskManagmentHandler as riskManagmentHandler


class TestGetStopLossFunction(unittest.TestCase):

    def setUp(self) -> None:
        log.PRINT_ERRORS = False

    def test_GetStopLoss(self):

        riskManagmentHandler.getMaxStopLossByPercent = MagicMock()
        riskManagmentHandler.getMaxStopLossByPercent.return_value = 8

        results = riskManagmentHandler.getStopLoss({}, 9, 10)
        self.assertEqual(results, 8)

    def test_GetStopLoss2(self):

        riskManagmentHandler.isStopLossExceeded = MagicMock()
        riskManagmentHandler.isStopLossExceeded.return_value = False

        results = riskManagmentHandler.getStopLoss(
            {'stopLossCanldes': 2}, 9, 10)
        self.assertEqual(results, 9)

    def test_GetStopLoss3(self):

        riskManagmentHandler.isStopLossExceeded = MagicMock()
        riskManagmentHandler.isStopLossExceeded.return_value = True

        riskManagmentHandler.getMaxStopLossByPercent = MagicMock()
        riskManagmentHandler.getMaxStopLossByPercent.return_value = 8

        results = riskManagmentHandler.getStopLoss(
            {'stopLossCanldes': 2}, 7, 10)
        self.assertEqual(results, 8)


if __name__ == '__main__':
    unittest.main()
