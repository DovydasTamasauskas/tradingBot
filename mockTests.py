# import unittest
# from unittest.mock import patch, MagicMock
# import ib_insync

# from ib import getHistoricalData
# from main import searchUnseenMessages


# class AA:
#     def reqHistoricalData():
#         return 'aa'


# class TestGetHistoricalData(unittest.TestCase):

#     @patch('ib.ib_insync.ib')
#     def test_getHistoricalData(self, mock_ib_insync):
#         mock = MagicMock()
#         mock.reqHistoricalData = ''
#         mock_ib_insync.reqHistoricalData = mock
#         self.assertEqual(getHistoricalData(AA, ''), 'aa')


# if __name__ == '__main__':
#     unittest.main()
