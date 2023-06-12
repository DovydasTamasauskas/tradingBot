import unittest
import shared.functions as functions
import shared.log as log


class TestGetTimeIntervalFunction(unittest.TestCase):

    def setUp(self) -> None:
        log.PRINT_WARNINGS = False

    def test_getTimeInterval(self):
        result = functions.getTimeInterval({"time": 17})

        self.assertEqual(result, 17)

    def test_getTimeInterval2(self):
        result = functions.getTimeInterval({"time": "19 mins"})

        self.assertEqual(result, 19)

    def test_getTimeInterval3(self):
        result = functions.getTimeInterval({"time": "19 ss"})

        self.assertEqual(result, 15)


if __name__ == '__main__':
    unittest.main()
