import unittest
import shared.functions as functions
import shared.log as log


class TestisRequiredParamsDefinedFunction(unittest.TestCase):

    def setUp(self) -> None:
        log.PRINT_WARNINGS = False

    def test_emply(self):
        json = functions.isRequiredParamsDefined({})
        self.assertFalse(json)

    def test_notAJson(self):
        json = functions.isRequiredParamsDefined(5)
        self.assertFalse(json)

    def test_noPosition(self):
        json = functions.isRequiredParamsDefined({
            "pair": "EURUSD",
            "size": 100,
            "time": "10:10:10"
        })
        self.assertFalse(json)

    def test_noPair(self):
        json = functions.isRequiredParamsDefined({
            "position": "long",
            "size": 100,
            "time": "10:10:10"
        })
        self.assertFalse(json)

    def test_noSize(self):
        json = functions.isRequiredParamsDefined({
            "position": "long",
            "pair": "EURUSD",
            "time": "10:10:10"
        })
        self.assertFalse(json)

    def test_noTime(self):
        json = functions.isRequiredParamsDefined({
            "position": "long",
            "pair": "EURUSD",
            "size": 100
        })
        self.assertFalse(json)

    def test_onlyRequired(self):
        json = functions.isRequiredParamsDefined({
            "position": "long",
            "pair": "EURUSD",
            "size": 100,
            "time": "10:10:10"
        })
        self.assertTrue(json)

    def test_moreThenRequired(self):
        json = functions.isRequiredParamsDefined({
            "position": "long",
            "pair": "EURUSD",
            "size": 100,
            "time": "10:10:10",
            "stopLossCanldes": 3,
            "maxStopLoss": "0.2",
        })
        self.assertTrue(json)


if __name__ == '__main__':
    unittest.main()
