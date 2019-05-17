import unittest
from typing import List


def compute_max(x: List[int]) -> int:
    pass


class Tests(unittest.TestCase):
    def test1(self):
        input_list = [1, 3, 5, 7]
        retval = compute_max(input_list)
        self.assertEqual(retval, 7)


unittest.main(verbosity=2)