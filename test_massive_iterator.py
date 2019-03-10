import unittest
from iterator_massive import MassiveIterator
from random import randint


class TestMassiveIterator(unittest.TestCase):
    @unittest.expectedFailure
    def test_empty_massive(self):
        MassiveIterator([])

    @unittest.expectedFailure
    def test_big_massive(self):
        MassiveIterator([1, 2, 3, 4])

    @unittest.expectedFailure
    def test_float(self):
        MassiveIterator([1.2])

    def test_only_end(self):
        self.assertEqual([i for i in range(0)], [i for i in MassiveIterator([0])])
        self.assertEqual([i for i in range(3)], [i for i in MassiveIterator([3])])
        self.assertEqual([i for i in range(-3)], [i for i in MassiveIterator([-3])])

    def test_start_end(self):
        self.assertEqual([i for i in range(1, 3)], [i for i in MassiveIterator([1, 3])])
        self.assertEqual([i for i in range(3, 3)], [i for i in MassiveIterator([3, 3])])
        self.assertEqual([i for i in range(3, 1)], [i for i in MassiveIterator([3, 1])])

    def test_start_end_step(self):
        self.assertEqual([i for i in range(1, 5, 2)], [i for i in MassiveIterator([1, 5, 2])])
        self.assertEqual([i for i in range(5, 1, -2)], [i for i in MassiveIterator([5, 1, -2])])

    def test_wrong_arguments(self):
        self.assertEqual([i for i in range(1, 5, -1)], [i for i in MassiveIterator([1, 5, -1])])
        self.assertEqual([i for i in range(5, 1, 1)], [i for i in MassiveIterator([5, 1, 1])])

    def test_random(self):
        for _ in range(10):
            stop = randint(1, 10000)
            self.assertEqual([i for i in range(stop)], [i for i in MassiveIterator([stop])])


if __name__ == '__main__':
    unittest.main()
