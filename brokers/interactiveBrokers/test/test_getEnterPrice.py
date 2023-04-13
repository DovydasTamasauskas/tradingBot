import unittest
import brokers.interactiveBrokers.handlePosition as handlePosition
import shared.log as log
from unittest.mock import MagicMock
import brokers.interactiveBrokers.api as api


class TestGetEnterPriceFunction(unittest.TestCase):

    def setUp(self) -> None:
        log.PRINT_ERRORS = False

    def test_enterPriceLimit(self):
        results = handlePosition.getEntryPrice('', {"limitPrice": 100})
        self.assertEqual(results, 100)

    def test_enterPriceLimit2(self):

        api.getMarketPrice = MagicMock()
        api.getMarketPrice.return_value = 105.5

        results = handlePosition.getEntryPrice('', {"limitPrice": 100})
        self.assertEqual(results, 100)

    def test_enterPriceMarket(self):

        api.getMarketPrice = MagicMock()
        api.getMarketPrice.return_value = 105.5

        results = handlePosition.getEntryPrice('', {})
        self.assertEqual(results, 105.5)


if __name__ == '__main__':
    unittest.main()
