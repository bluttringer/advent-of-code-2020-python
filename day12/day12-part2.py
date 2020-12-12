import re

def extract(line):
    groups = re.search('(\w)(\d+)', line)
    return (groups[1], int(groups[2]))

def rotateClockwise(vector):
    return (vector[1], -vector[0])

def rotateAntiClockwise(vector):
    return (-vector[1], vector[0])

def move(vector, east, north):
    return (vector[0] + east, vector[1] + north)

f = open('input.data')
data = [extract(line) for line in f.readlines()]
print(*data)

east = 0
north = 0
waypoint = (10, 1)

for instruction in data:
    cdir = instruction[0]
    cval = instruction[1]

    if cdir == 'F':
        east += cval * waypoint[0]
        north += cval * waypoint[1]
    # rotate waypointint()
    elif cdir == 'R':
        for i in range(int(cval / 90)):
            waypoint = rotateClockwise(waypoint)
    elif cdir == 'L':
        for i in range(int(cval / 90)):
            waypoint = rotateAntiClockwise(waypoint)
    else:
        if cdir == 'E':
            waypoint = move(waypoint, cval, 0)
        elif cdir == 'W':
            waypoint = move(waypoint, -cval, 0)
        elif cdir == 'N':
            waypoint = move(waypoint, 0, cval)
        elif cdir == 'S':
            waypoint = move(waypoint, 0, -cval)
    print('instruction = ', instruction)

print('result = ', abs(east) + abs(north))

