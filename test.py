import unittest
from main import slice
from main import toJson
from main import isBotMessage


class TestSlice(unittest.TestCase):
    def test_slice(self):
        self.assertEqual(slice("testas", 1, 3), "es")


class TestToJson(unittest.TestCase):
    def test_to_json(self):
        self.assertEqual(
            toJson('BOT{"position": "long"}'), {"position": "long"})


class TestIsBotMessage(unittest.TestCase):
    def test_is_bot_message(self):
        self.assertEqual(
            isBotMessage('BOT{"position": "long"}'), True)


class TestIsBotMessage2(unittest.TestCase):
    def test_is_bot_message2(self):
        self.assertEqual(
            isBotMessage('{"position": "long"}'), False)


class TestIsBotMessage3(unittest.TestCase):
    def test_is_bot_message3(self):
        self.assertEqual(
            isBotMessage('BOOT{"position": "long"}'), False)


if __name__ == '__main__':
    unittest.main()
