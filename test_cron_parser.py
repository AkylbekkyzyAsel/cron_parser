import unittest
from cron_parser import parse_field


class TestParseField(unittest.TestCase):

    def test_parse_field_all(self):
        result = parse_field('*', 0, 59)
        self.assertEqual(result, list(range(60)))

    def test_parse_field_single(self):
        result = parse_field('5', 0, 59)
        self.assertEqual(result, [5])

    def test_parse_field_range(self):
        result = parse_field('10-15', 0, 59)
        self.assertEqual(result, list(range(10, 16)))

    def test_parse_field_multi(self):
        result = parse_field('1,15', 0, 59)
        self.assertEqual(result, [1, 15])

    def test_parse_field_increment_all(self):
        result = parse_field('*/1', 0, 59)
        self.assertEqual(result, list(range(60)))

    def test_parse_field_increment(self):
        result = parse_field('*/15', 0, 59)
        self.assertEqual(result, [0, 15, 30, 45])

    def test_parse_field_increment_start(self):
        result = parse_field('5/15', 0, 59)
        self.assertEqual(result, [5])
