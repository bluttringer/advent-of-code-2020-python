from space import Space

def main(filename):
    data = open(filename).readlines()
    space3 = Space(3)
    for i, row in enumerate(data):
        for j, state in enumerate(row.strip()):
                space3.updateCube((i, j, 0), state)

    for _ in range(6):
        space3.runIterations()

    print(f'part1 : nb active cubes = {space3.countActiveCubes()}')

    space4 = Space(4)
    for i, row in enumerate(data):
        for j, state in enumerate(row.strip()):
                space4.updateCube((i, j, 0, 0), state)

    for _ in range(6):
        space4.runIterations()

    print(f'part2 : nb active cubes = {space4.countActiveCubes()}')

if __name__ == '__main__':
    main('day17/input.data')