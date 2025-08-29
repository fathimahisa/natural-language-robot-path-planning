import unittest
from path_planner import astar

GRID = [
    [0,0,0,0],
    [0,1,1,0],
    [0,0,0,0],
    [0,0,0,0],
]

class TestPlanner(unittest.TestCase):
    def test_simple_path(self):
        path = astar(GRID, (0,0), (0,3))
        self.assertTrue(len(path) > 0)
        self.assertEqual(path[-1], (0,3))

if __name__ == "__main__":
    unittest.main()
