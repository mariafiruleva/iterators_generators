import unittest
from iterator_massive import RangeIterator
from random import randint


class TestMassiveIterator(unittest.TestCase):
    @unittest.expectedFailure
    def test_empty_massive(self):
        RangeIterator()

    @unittest.expectedFailure
    def test_big_massive(self):
        RangeIterator(1, 2, 3, 4)

    @unittest.expectedFailure
    def test_float(self):
        RangeIterator(1.2)

    @unittest.expectedFailure
    def test_zero_step(self):
        RangeIterator(1, 2, 0)

    def test_only_end(self):
        self.assertEqual([i for i in range(0)], [i for i in RangeIterator(0)])
        self.assertEqual([i for i in range(3)], [i for i in RangeIterator(3)])
        self.assertEqual([i for i in range(-3)], [i for i in RangeIterator(-3)])

    def test_start_end(self):
        self.assertEqual([i for i in range(1, 3)], [i for i in RangeIterator(1, 3)])
        self.assertEqual([i for i in range(3, 3)], [i for i in RangeIterator(3, 3)])
        self.assertEqual([i for i in range(3, 1)], [i for i in RangeIterator(3, 1)])

    def test_start_end_step(self):
        self.assertEqual([i for i in range(1, 5, 2)], [i for i in RangeIterator(1, 5, 2)])
        self.assertEqual([i for i in range(5, 1, -2)], [i for i in RangeIterator(5, 1, -2)])

    def test_wrong_arguments(self):
        self.assertEqual([i for i in range(1, 5, -1)], [i for i in RangeIterator(1, 5, -1)])
        self.assertEqual([i for i in range(5, 1, 1)], [i for i in RangeIterator(5, 1, 1)])

    def test_long_arguments(self):
        self.assertEqual([i for i in range(1, 100000, 1)], [i for i in RangeIterator(1, 100000, 1)])
        self.assertEqual([i for i in range(1, 100000, 2)], [i for i in RangeIterator(1, 100000, 2)])
        self.assertEqual([i for i in range(1, -100000, -1)], [i for i in RangeIterator(1, -100000, -1)])
        self.assertEqual([i for i in range(1, -100000, -2)], [i for i in RangeIterator(1, -100000, -2)])

    def test_random(self):
        for _ in range(10):
            stop = randint(1, 10000)
            self.assertEqual([i for i in range(stop)], [i for i in RangeIterator(stop)])


if __name__ == '__main__':
    unittest.main()
