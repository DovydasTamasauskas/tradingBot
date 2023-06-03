import unittest
import handlers.riskManagmentHandler as riskManagmentHandler
import shared.log as log


class TestStopLossPercentFunction(unittest.TestCase):

    def setUp(self) -> None:
        log.PRINT_WARNINGS = False

    def test_getStopLoss1(self):
        stopLoss = riskManagmentHandler.getMaxStopLossByPercent({
            "position": "long",
            "stopLossPercent": 1,
            "enteryPrice": 1,
        })
        self.assertEqual(stopLoss, 0.99)

    def test_getStopLoss2(self):
        stopLoss = riskManagmentHandler.getMaxStopLossByPercent({
            "position": "long",
            "stopLossPercent": 2,
            "enteryPrice": 1,
        })
        self.assertEqual(stopLoss, 0.98)

    def test_getStopLoss3(self):
        stopLoss = riskManagmentHandler.getMaxStopLossByPercent({
            "position": "long",
            "stopLossPercent": 0.5,
            "enteryPrice": 100,
        })
        self.assertEqual(stopLoss, 99.5)

    def test_getStopLoss4(self):
        stopLoss = riskManagmentHandler.getMaxStopLossByPercent({
            "position": "long",
            "enteryPrice": 100,
        })
        self.assertEqual(stopLoss, 99)

    def test_getStopLoss5(self):
        stopLoss = riskManagmentHandler.getMaxStopLossByPercent({
            "position": "short",
            "stopLossPercent": 1,
            "enteryPrice": 100,
        })

        self.assertEqual(stopLoss, 101)

    def test_getStopLoss6(self):
        stopLoss = riskManagmentHandler.getMaxStopLossByPercent({
            "position": "short",
            "stopLossPercent": 0.5,
            "enteryPrice": 100,
        })
        self.assertEqual(stopLoss, 100.5)

    def test_getStopLoss7(self):
        stopLoss = riskManagmentHandler.getMaxStopLossByPercent({
            "position": "short",
            "stopLossPercent": 2,
            "enteryPrice": 100,
        })
        self.assertEqual(stopLoss, 102)

    def test_getStopLoss8(self):
        stopLoss = riskManagmentHandler.getMaxStopLossByPercent({
            "position": "short",
            "enteryPrice": 100,
        })
        self.assertEqual(stopLoss, 101)


if __name__ == '__main__':
    unittest.main()
