import unittest
import shared.functions as functions
import shared.log as log


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self) -> None:
        log.PRINT_WARNINGS = False

    def test_middleSlice(self):
        sliced = functions.slice("123456789", 1, 5)

        self.assertEqual(sliced, "2345")

    def test_startSlice(self):
        sliced = functions.slice("123456789", 0, 5)

        self.assertEqual(sliced, "12345")

    def test_startSlice2(self):
        sliced = functions.slice("123456789", end=5)

        self.assertEqual(sliced, "12345")

    def test_endSlice(self):
        sliced = functions.slice("123456789", 2)

        self.assertEqual(sliced, "3456789")

    def test_endSlice2(self):
        sliced = functions.slice("123456789", 2, 20)

        self.assertEqual(sliced, "3456789")


if __name__ == '__main__':
    unittest.main()
