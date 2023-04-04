import unittest
import handlers.riskManagmentHandler as riskManagmentHandler
import shared.log as log


class TestTakeProfitFunction(unittest.TestCase):

    def setUp(self) -> None:
        log.PRINT_WARNINGS = False

    def test_getTakeProfit1(self):
        takeProfit = riskManagmentHandler.getTakeProfit({
            "takeProfitRatio": 1.5,
            "enteryPrice": 100,
            "stopLoss": 98,
        })

        self.assertEqual(takeProfit, 103)

    def test_getTakeProfit2(self):
        takeProfit = riskManagmentHandler.getTakeProfit({
            "takeProfitRatio": 2.5,
            "enteryPrice": 100,
            "stopLoss": 99,
        })

        self.assertEqual(takeProfit, 102.5)

    def test_getTakeProfit3(self):
        takeProfit = riskManagmentHandler.getTakeProfit({
            "takeProfitRatio": 3,
            "enteryPrice": 100,
            "stopLoss": 102,
        })

        self.assertEqual(takeProfit, 94)

    def test_getTakeProfit4(self):
        takeProfit = riskManagmentHandler.getTakeProfit({
            "takeProfitRatio": 3.5,
            "enteryPrice": 100,
            "stopLoss": 101,
        })

        self.assertEqual(takeProfit, 96.5)


if __name__ == '__main__':
    unittest.main()
