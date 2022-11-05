import unittest
from sum import sum


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(1, 2), 3)
        self.assertEqual(sum(-1, -1), -2)
        self.assertEqual(sum(2, -1), 1)


if __name__ == '__main__':
    unittest.main()
