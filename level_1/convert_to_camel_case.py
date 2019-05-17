from typing import List


def convert_to_camel_case(word: str) -> str:
    pass


import unittest


class Tests(unittest.TestCase):
    def test1(self):
        input_word = "MillBurn"
        retval = convert_to_camel_case(input_word)
        expected_word = "millBurn"
        self.assertEqual(retval, expected_word)


unittest.main(verbosity=2)