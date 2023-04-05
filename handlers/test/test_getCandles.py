import unittest
import handlers.riskManagmentHandler as riskManagmentHandler
import shared.log as log


class TestGetCandlesFunction(unittest.TestCase):

    def setUp(self) -> None:
        log.PRINT_WARNINGS = False

    def test_getCandles1(self):
        low = riskManagmentHandler.getCandlesLow(
            [{'low': 99}, {'low': 99.5}, {'low': 101}, {'low': 200}, {'low': 111}, {'low': 222}])
        self.assertEqual(low, 99)

    def test_getCandles2(self):
        low = riskManagmentHandler.getCandlesLow(
            [{'low': 99}, {'low': 99.5}, {'low': 101}, {'low': 95.5}, {'low': 111}, {'low': 222}])
        self.assertEqual(low, 95.5)

    def test_getCandles3(self):
        high = riskManagmentHandler.getCandlesHigh(
            [{'high': 99}, {'high': 99.5}, {'high': 101}, {'high': 200}, {'high': 111}, {'high': 222}])
        self.assertEqual(high, 222)

    def test_getCandles4(self):
        high = riskManagmentHandler.getCandlesHigh(
            [{'high': 99}, {'high': 99.5}, {'high': 223.5}, {'high': 95.5}, {'high': 111}, {'high': 222}])
        self.assertEqual(high, 223.5)


if __name__ == '__main__':
    unittest.main()
