import unittest
import brokers.interactiveBrokers.handlePosition as handlePosition
import shared.log as log
from unittest.mock import MagicMock
import brokers.interactiveBrokers.api as api


class TestGetContractFunction(unittest.TestCase):

    def setUp(self) -> None:
        log.PRINT_ERRORS = False

    def test_getContract1(self):
        api.setForexContract = MagicMock()
        api.setForexContract.return_value = "fiat"
        results = handlePosition.getContract({"pair": "EURUSD"})
        self.assertEqual(results, "fiat")

    def test_getContract2(self):
        api.setCryptoContract = MagicMock()
        api.setCryptoContract.return_value = "crypto"
        results = handlePosition.getContract({"pair": "BTC"})
        self.assertEqual(results, "crypto")

    def test_getContract3(self):
        api.setStockContract = MagicMock()
        api.setStockContract.return_value = "stock"
        results = handlePosition.getContract({"pair": "TSLA"})
        self.assertEqual(results, "stock")

    def test_getContract4(self):
        results = handlePosition.getContract({"pair": "aaa"})
        self.assertEqual(results, None)


if __name__ == '__main__':
    unittest.main()
