import unittest
from stockanalysis.utils.conversion_type import get_conversion_type


class UtilsTest(unittest.TestCase):
    def test_get_conversion_type(self):
        conversion_type = "what_if"
        result = get_conversion_type(conversion_type)
        self.assertIsNotNone(result)
