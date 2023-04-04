import unittest
import handlers.riskManagmentHandler as riskManagmentHandler
import shared.log as log


class TestStopLossHistoricalFunction(unittest.TestCase):

    def setUp(self) -> None:
        log.PRINT_WARNINGS = False

    def test_getStopLoss1(self):
        stopLoss = riskManagmentHandler.getStopLossHistorical([{'low': 100, 'high': 110}, {'low': 101, 'high': 111}, {'low': 102, 'high': 112}], {
            "position": "long",
        })

        self.assertEqual(stopLoss, 100)

    def test_getStopLoss2(self):
        stopLoss = riskManagmentHandler.getStopLossHistorical([{'low': 100, 'high': 110}, {'low': 99.5, 'high': 111}, {'low': 102, 'high': 112}], {
            "position": "long",
        })

        self.assertEqual(stopLoss, 99.5)

    def test_getStopLoss3(self):
        stopLoss = riskManagmentHandler.getStopLossHistorical([{'low': 100, 'high': 110}, {'low': 99.5, 'high': 111}, {'low': 102, 'high': 112}], {
            "position": "short",
        })

        self.assertEqual(stopLoss, 112)

    def test_getStopLoss4(self):
        stopLoss = riskManagmentHandler.getStopLossHistorical([{'low': 100, 'high': 110}, {'low': 99.5, 'high': 130.5}, {'low': 102, 'high': 112}], {
            "position": "short",
        })

        self.assertEqual(stopLoss, 130.5)

    def test_getStopLoss5(self):
        stopLoss = riskManagmentHandler.getStopLossHistorical([{'low': 100, 'high': 110}, {'low': 99.5, 'high': 130.44444444}, {'low': 102, 'high': 112}], {
            "position": "short",
        })

        self.assertEqual(stopLoss, 130.44444)


if __name__ == '__main__':
    unittest.main()
