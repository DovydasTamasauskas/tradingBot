import unittest
import handlers.riskManagmentHandler as riskManagmentHandler
import shared.log as log


class TestIsStopLossExceededFunction(unittest.TestCase):

    def setUp(self) -> None:
        log.PRINT_WARNINGS = False

    def test_isStopLossExceeded1(self):
        results = riskManagmentHandler.isStopLossExceeded({
            "maxStopLoss": 2,
        }, 101, 100)

        self.assertFalse(results)

    def test_isStopLossExceeded2(self):
        results = riskManagmentHandler.isStopLossExceeded({
            "maxStopLoss": 2,
        }, 103, 100)
        self.assertTrue(results)

    def test_isStopLossExceeded3(self):
        results = riskManagmentHandler.isStopLossExceeded({
            "maxStopLoss": 1.5,
        }, 103, 100)
        self.assertTrue(results)

    def test_isStopLossExceeded4(self):
        results = riskManagmentHandler.isStopLossExceeded({
            "maxStopLoss": 2,
        }, 101.5, 100)
        self.assertFalse(results)

    def test_isStopLossExceeded5(self):
        results = riskManagmentHandler.isStopLossExceeded({}, 101.5, 100)
        self.assertTrue(results)

    def test_isStopLossExceeded6(self):
        results = riskManagmentHandler.isStopLossExceeded({}, 99.5, 100)
        self.assertFalse(results)

    def test_isStopLossExceeded7(self):
        results = riskManagmentHandler.isStopLossExceeded({}, 98.5, 100)
        self.assertTrue(results)


if __name__ == '__main__':
    unittest.main()
