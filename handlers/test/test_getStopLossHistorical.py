import unittest
import handlers.riskManagmentHandler as riskManagmentHandler
import shared.log as log
from unittest.mock import MagicMock


class TestStopLossHistoricalFunction(unittest.TestCase):

    def setUp(self) -> None:
        log.PRINT_WARNINGS = False

    def test_getStopLoss1(self):
        riskManagmentHandler.isStopLossExceeded = MagicMock()
        riskManagmentHandler.isStopLossExceeded.return_value = False
        stopLoss = riskManagmentHandler.getStopLossHistorical([{'low': 99}, {'low': 99.5}], {
            "position": "long",
            "enteryPrice": 100,
            "stopLossCanldes": 2,
            "maxStopLoss": 2,
        })
        self.assertEqual(stopLoss, 99)

    def test_getStopLoss2(self):
        riskManagmentHandler.isStopLossExceeded = MagicMock()
        riskManagmentHandler.isStopLossExceeded.return_value = True
        stopLoss = riskManagmentHandler.getStopLossHistorical([{'low': 97}, {'low': 96}], {
            "position": "long",
            "enteryPrice": 100,
            "stopLossCanldes": 2,
            "maxStopLoss": 2,
        })
        self.assertEqual(stopLoss, 98)

    def test_getStopLoss3(self):
        riskManagmentHandler.isStopLossExceeded = MagicMock()
        riskManagmentHandler.isStopLossExceeded.return_value = True
        stopLoss = riskManagmentHandler.getStopLossHistorical([{'high': 103}, {'high': 102}], {
            "position": "short",
            "enteryPrice": 100,
            "stopLossCanldes": 2,
            "maxStopLoss": 1.5,
        })
        self.assertEqual(stopLoss, 101.5)

    def test_getStopLoss4(self):
        riskManagmentHandler.isStopLossExceeded = MagicMock()
        riskManagmentHandler.isStopLossExceeded.return_value = False
        stopLoss = riskManagmentHandler.getStopLossHistorical([{'high': 101}, {'high': 101}], {
            "position": "short",
            "enteryPrice": 100,
            "stopLossCanldes": 2,
            "maxStopLoss": 2,
        })
        self.assertEqual(stopLoss, 101)

    def test_getStopLoss5(self):
        riskManagmentHandler.isStopLossExceeded = MagicMock()
        riskManagmentHandler.isStopLossExceeded.return_value = True
        stopLoss = riskManagmentHandler.getStopLossHistorical([{'high': 110}, {'high': 109}], {
            "position": "short",
            "enteryPrice": 100,
            "stopLossCanldes": 2,
            "maxStopLoss": 2,
        })
        self.assertEqual(stopLoss, 102)

    def test_getStopLoss5(self):
        riskManagmentHandler.isStopLossExceeded = MagicMock()
        riskManagmentHandler.isStopLossExceeded.return_value = False
        stopLoss = riskManagmentHandler.getStopLossHistorical([{'high': 110}, {'high': 109}, {'high': 101}, {'high': 101.5}], {
            "position": "short",
            "enteryPrice": 100,
            "stopLossCanldes": 2,
            "maxStopLoss": 2,
        })
        self.assertEqual(stopLoss, 101.5)

    def test_getStopLoss6(self):
        riskManagmentHandler.isStopLossExceeded = MagicMock()
        riskManagmentHandler.isStopLossExceeded.return_value = False
        stopLoss = riskManagmentHandler.getStopLossHistorical([{'low': 90}, {'low': 91.5}, {'low': 99}, {'low': 99.5}], {
            "position": "long",
            "enteryPrice": 100,
            "stopLossCanldes": 2,
            "maxStopLoss": 2,
        })
        self.assertEqual(stopLoss, 99)

    def test_getStopLoss7(self):
        riskManagmentHandler.isStopLossExceeded = MagicMock()
        riskManagmentHandler.isStopLossExceeded.return_value = True
        stopLoss = riskManagmentHandler.getStopLossHistorical([{'high': 110}], {
            "position": "short",
            "enteryPrice": 100,
            "stopLossCanldes": 3,
            "maxStopLoss": 2,
        })
        self.assertEqual(stopLoss, 102)

    def test_getStopLoss8(self):
        riskManagmentHandler.isStopLossExceeded = MagicMock()
        riskManagmentHandler.isStopLossExceeded.return_value = True
        stopLoss = riskManagmentHandler.getStopLossHistorical([{'low': 90}], {
            "position": "long",
            "enteryPrice": 100,
            "stopLossCanldes": 3,
            "maxStopLoss": 2,
        })
        self.assertEqual(stopLoss, 98)

    def test_getStopLoss9(self):
        riskManagmentHandler.isStopLossExceeded = MagicMock()
        riskManagmentHandler.isStopLossExceeded.return_value = False
        stopLoss = riskManagmentHandler.getStopLossHistorical([{'high': 110}, {'high': 101}, {'high': 100.5}, {'high': 101.5}], {
            "position": "short",
            "enteryPrice": 100,
            "maxStopLoss": 2,
        })
        self.assertEqual(stopLoss, 101.5)

    def test_getStopLoss10(self):
        riskManagmentHandler.isStopLossExceeded = MagicMock()
        riskManagmentHandler.isStopLossExceeded.return_value = False
        stopLoss = riskManagmentHandler.getStopLossHistorical([{'low': 90}, {'low': 99}, {'low': 99.5}, {'low': 98.5}], {
            "position": "long",
            "enteryPrice": 100,
            "stopLossCanldes": 3,
            "maxStopLoss": 2,
        })
        self.assertEqual(stopLoss, 98.5)

    def test_getStopLoss11(self):
        riskManagmentHandler.isStopLossExceeded = MagicMock()
        riskManagmentHandler.isStopLossExceeded.return_value = False
        stopLoss = riskManagmentHandler.getStopLossHistorical([{'high': 100.5}, {'high': 100.2}], {
            "position": "short",
            "enteryPrice": 100,
        })
        self.assertEqual(stopLoss, 100.5)

    def test_getStopLoss12(self):
        riskManagmentHandler.isStopLossExceeded = MagicMock()
        riskManagmentHandler.isStopLossExceeded.return_value = False
        stopLoss = riskManagmentHandler.getStopLossHistorical([{'low': 99.5}, {'low': 99.7}], {
            "position": "long",
            "enteryPrice": 100,
        })
        self.assertEqual(stopLoss, 99.5)

    def test_getStopLoss13(self):
        riskManagmentHandler.isStopLossExceeded = MagicMock()
        riskManagmentHandler.isStopLossExceeded.return_value = True
        stopLoss = riskManagmentHandler.getStopLossHistorical([{'high': 101.5}, {'high': 101.2}], {
            "position": "short",
            "enteryPrice": 100,
        })
        self.assertEqual(stopLoss, 101)

    def test_getStopLoss14(self):
        riskManagmentHandler.isStopLossExceeded = MagicMock()
        riskManagmentHandler.isStopLossExceeded.return_value = True
        stopLoss = riskManagmentHandler.getStopLossHistorical([{'low': 98.5}, {'low': 98.7}], {
            "position": "long",
            "enteryPrice": 100,
        })
        self.assertEqual(stopLoss, 99)


if __name__ == '__main__':
    unittest.main()
