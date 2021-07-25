import unittest
from main import Wires

test_wires = Wires('test_input1.txt')


class MainTestCase(unittest.TestCase):
    def test_parse(self):
        wire_1 = test_wires.wire_1
        direction, length = test_wires.parse(wire_1[0])
        self.assertEqual(direction, 'R')
        self.assertEqual(length, 8)

    def test_get_grid(self):
        grid = test_wires.grid
        self.assertEqual(len(grid), 41)

        dim = test_wires.get_grid_dimensions(grid)
        self.assertEqual(dim[0], 8)
        self.assertEqual(dim[1], 7)

        test_wires.print_grid(grid)


if __name__ == '__main__':
    unittest.main()
