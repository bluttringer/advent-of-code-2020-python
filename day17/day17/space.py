import copy
from collections import defaultdict
from itertools import product

class Space:

    ACTIVE = '#'
    INACTIVE = '.'

    def __init__(self, d):
        # space is a d-dimension one
        self.__space = defaultdict(lambda: Space.INACTIVE)
        self.__dimensions = d

    def updateCube(self, coordinates, state):
        self.__space[coordinates] = state

    def neighborsCoordinates(self, *coordinates: int):
        # neighbors = cubes that are at distance 1 of the current cube along each dimension
        for diff in product([-1,0,1], repeat=len(coordinates)):
            coordinate = tuple(c + diff[i] for i,c in enumerate(coordinates))
            yield coordinate

    def runIterations(self):
        cubeActiveCounts = defaultdict(int)
        for cube, state in list(self.__space.items()):
            for neighbor in self.neighborsCoordinates(*cube):
                if state == Space.ACTIVE:
                    cubeActiveCounts[neighbor] += neighbor != cube

        for n, count in cubeActiveCounts.items():
            if self.__space[n] == Space.ACTIVE:
                if count in (2,3):
                    self.__space[n] = Space.ACTIVE
                else:
                    self.__space[n] = Space.INACTIVE
            elif self.__space[n] == Space.INACTIVE:
                if count == 3:
                    self.__space[n] = Space.ACTIVE

    def countActiveCubes(self):
        return sum(state == Space.ACTIVE for state in self.__space.values())
    