import unittest
import brokers.interactiveBrokers.handlePosition as handlePosition
import shared.log as log
from unittest.mock import MagicMock
import brokers.interactiveBrokers.api as api


class TestGetStopLossByCandlesFunction(unittest.TestCase):

    def setUp(self) -> None:
        log.PRINT_ERRORS = False

    def test_StopLossHistorical(self):
        handlePosition.getContract = MagicMock()
        handlePosition.getContract.return_value = 0

        api.getHistoricalData = MagicMock()
        api.getHistoricalData.return_value = [{'high': 99}, {'high': 99.5}, {
            'high': 101}, {'high': 200}, {'high': 111}, {'high': 222}]

        handlePosition.getStopLossHistorical = MagicMock()
        handlePosition.getStopLossHistorical.return_value = 10

        results = handlePosition.getStopLossByCandles(
            '', {"stopLossCanldes": 4})
        self.assertEqual(results, 10)


if __name__ == '__main__':
    unittest.main()
