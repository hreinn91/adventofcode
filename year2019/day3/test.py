import unittest
from main import Wires
from main import norm_l1

wires = Wires('test_input1.txt')


class MainTestCase(unittest.TestCase):
    def test_parse(self):
        wire_1 = wires.wire_1
        direction, length = wires.parse(wire_1[0])
        self.assertEqual(direction, 'R')
        self.assertEqual(length, 8)

    def test_norm_l1(self):
        self.assertEqual(norm_l1(3, 3), 6)
        self.assertEqual(norm_l1(-3, 3), 6)
        self.assertEqual(norm_l1(2, 9), 11)

    def test_get_grid(self):
        grid = wires.grid
        wires.print_grid(grid)
        self.assertEqual(len(grid), 41)

        dim = wires.get_grid_dimensions(grid)
        self.assertEqual(dim[0], 8)
        self.assertEqual(dim[1], 7)

        intersections = wires.intersections
        self.assertEqual(len(intersections), 2)

        manhattan_distance = wires.get_shortest_intersection(intersections)
        self.assertEqual(manhattan_distance, 6)



if __name__ == '__main__':
    unittest.main()
