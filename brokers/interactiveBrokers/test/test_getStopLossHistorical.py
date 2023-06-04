import unittest
import brokers.interactiveBrokers.handlePosition as handlePosition
import shared.log as log
from unittest.mock import MagicMock


class TestStopLossHistoricalFunction(unittest.TestCase):

    def setUp(self) -> None:
        log.PRINT_WARNINGS = False

    def test_getStopLoss1(self):
        stopLoss = handlePosition.getStopLossHistorical([{'low': 99}, {'low': 99.5}], {
            "position": "long",
            "stopLossCanldes": 2,
        })
        self.assertEqual(stopLoss, 99)

    def test_getStopLoss2(self):
        stopLoss = handlePosition.getStopLossHistorical([{'high': 103}, {'high': 102}], {
            "position": "short",
            "stopLossCanldes": 2,
        })
        self.assertEqual(stopLoss, 103)

    def test_getStopLoss3(self):
        stopLoss = handlePosition.getStopLossHistorical([{'high': 110}, {'high': 109}, {'high': 103}, {'high': 101.5}], {
            "position": "short",
            "stopLossCanldes": 2,
        })
        self.assertEqual(stopLoss, 103)

    def test_getStopLoss4(self):
        stopLoss = handlePosition.getStopLossHistorical([{'low': 90}, {'low': 91.5}, {'low': 99}, {'low': 99.5}], {
            "position": "long",
            "stopLossCanldes": 2,
        })
        self.assertEqual(stopLoss, 99)


if __name__ == '__main__':
    unittest.main()
