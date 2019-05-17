from typing import List


def bsearch(inp_list: List[int], item:int) -> bool:


import unittest


class Tests(unittest.TestCase):
    def test1(self):
        input_list = [1, 3, 12, -3, 4, 15, 7]
        item_list = [4, 5]
        ans_list = [True, False]
        for i, v in enumerate(item_list):
            retval = bsearch(input_list, v)
            expected = ans_list[i]
            self.assertEqual(retval, expected)


unittest.main(verbosity=2)