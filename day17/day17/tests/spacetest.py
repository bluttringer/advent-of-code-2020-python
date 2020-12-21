import sys, os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import unittest
from space import Space


class SpaceTest(unittest.TestCase):

    def test_should_find_neighbors(self):
        space = Space(3)
        neighbors = [ n for n in space.neighborsCoordinates(0,0,0) ]
        self.assertCountEqual(neighbors, [
            (-1,0,0),(-1,1,0),(0,1,0),(1,1,0),(1,0,0),(1,-1,0),(0,-1,0),(-1,-1,0),
            (0,0,-1),(-1,0,-1),(-1,1,-1),(0,1,-1),(1,1,-1),(1,0,-1),(1,-1,-1),(0,-1,-1),(-1,-1,-1),
            (0,0,1),(-1,0,1),(-1,1,1),(0,1,1),(1,1,1),(1,0,1),(1,-1,1),(0,-1,1),(-1,-1,1)
        ])

if __name__ == '__main__':
    unittest.main()