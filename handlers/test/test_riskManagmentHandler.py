import unittest
import handlers.riskManagmentHandler as riskManagmentHandler
import shared.log as log


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self) -> None:
        log.PRINT_WARNINGS = False

    def test_getStopLoss1(self):
        stopLoss = riskManagmentHandler.getStopLoss([], {
            "position": "long",
            "stopLossPercent": 1,
            "enteryPrice": 1,

        })

        self.assertEqual(stopLoss, 0.99)

    def test_getStopLoss2(self):
        stopLoss = riskManagmentHandler.getStopLoss([], {
            "position": "long",
            "stopLossPercent": 2,
            "enteryPrice": 1,

        })

        self.assertEqual(stopLoss, 0.98)

    def test_getStopLoss3(self):
        stopLoss = riskManagmentHandler.getStopLoss([], {
            "position": "long",
            "stopLossPercent": 3,
            "enteryPrice": 50,

        })

        self.assertEqual(stopLoss, 48.5)

    def test_getStopLoss4(self):
        stopLoss = riskManagmentHandler.getStopLoss([], {
            "position": "short",
            "stopLossPercent": 1,
            "enteryPrice": 1,

        })

        self.assertEqual(stopLoss, 1.01)

    def test_getStopLoss5(self):
        stopLoss = riskManagmentHandler.getStopLoss([], {
            "position": "short",
            "stopLossPercent": 2,
            "enteryPrice": 1,

        })

        self.assertEqual(stopLoss, 1.02)

    def test_getStopLoss6(self):
        stopLoss = riskManagmentHandler.getStopLoss([], {
            "position": "short",
            "stopLossPercent": 3,
            "enteryPrice": 50,

        })

        self.assertEqual(stopLoss, 51.5)


if __name__ == '__main__':
    unittest.main()
