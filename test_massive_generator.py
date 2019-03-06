import unittest
from generator_massive import MassiveGenerator


class TestMassiveGenerator(unittest.TestCase):
    @unittest.expectedFailure
    def test_empty_massive(self):
        MassiveGenerator([])

    @unittest.expectedFailure
    def test_big_massive(self):
        MassiveGenerator([1, 2, 3, 4])

    def test_only_end(self):
        self.assertEqual([i for i in range(0)], [i for i in MassiveGenerator([0])])
        self.assertEqual([i for i in range(3)], [i for i in MassiveGenerator([3])])
        self.assertEqual([i for i in range(-3)], [i for i in MassiveGenerator([-3])])

    def test_start_end(self):
        self.assertEqual([i for i in range(1, 3)], [i for i in MassiveGenerator([1, 3])])
        self.assertEqual([i for i in range(3, 3)], [i for i in MassiveGenerator([3, 3])])
        self.assertEqual([i for i in range(3, 1)], [i for i in MassiveGenerator([3, 1])])

    def test_start_end_step(self):
        self.assertEqual([i for i in range(1, 5, 2)], [i for i in MassiveGenerator([1, 5, 2])])
        self.assertEqual([i for i in range(5, 1, -2)], [i for i in MassiveGenerator([5, 1, -2])])

    def test_wrong_arguments(self):
        self.assertEqual([i for i in range(1, 5, -1)], [i for i in MassiveGenerator([1, 5, -1])])
        self.assertEqual([i for i in range(5, 1, 1)], [i for i in MassiveGenerator([5, 1, 1])])


if __name__ == '__main__':
    unittest.main()
