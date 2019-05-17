import unittest


def addone(x: int) -> int:
    pass


class Tests(unittest.TestCase):
    def test1(self):
        input_val = 3
        retval = addone(input_val)
        self.assertEqual(retval, 4)


unittest.main(verbosity=2)