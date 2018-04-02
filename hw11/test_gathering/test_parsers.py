import unittest
from parsers.get_datetime import parse_date
from datetime import datetime, timedelta


TEST_DATETIME = [["сегодня в 17:37", datetime.today().replace(hour=17, minute=37, second=0, microsecond=0)],
                 ["вчера в 17:37", (datetime.today().replace(
                                            hour=17, minute=37, second=0, microsecond=0) - timedelta(days=1))],
                 ["16 июля 2015 в 12:42", datetime.today().replace(
                                        day=16, month=7, year=2015, hour=12, minute=42, second=0, microsecond=0)],
                 ["18 октября в 09:29", datetime.today().replace(
                                        day=18, month=10, hour=9, minute=29, second=0, microsecond=0)],
                 [" 4 ноября в 20:16", datetime.today().replace(
                                        day=4, month=11, hour=20, minute=16, second=0, microsecond=0)],
                 ["28 августа в 09:00", datetime.today().replace(
                                        day=28, month=8, hour=9, minute=0, second=0, microsecond=0)],
                 [" 1 декабря 2013 в 00:31", datetime.today().replace(
                                        day=1, month=12, year=2013, hour=0, minute=31, second=0, microsecond=0)]]


class TestDatetimeParser(unittest.TestCase):
    def test_parse(self):
        for DATE_TEST in TEST_DATETIME:
            self.assertEqual(parse_date([DATE_TEST[0]]), DATE_TEST[1])


if __name__ == '__main__':
    unittest.main()
