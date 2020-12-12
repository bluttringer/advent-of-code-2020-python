import re

def extract(line):
    groups = re.search('(\w)(\d+)', line)
    return (groups[1], int(groups[2]))

f = open('input.data')
data = [extract(line) for line in f.readlines()]
print(*data)

east = 0
north = 0
direction = 'E'
directions =[ 'E', 'S', 'W', 'N' ]

for instruction in data:
    cdir = instruction[0]
    cval = instruction[1]

    if cdir == 'F':
        if direction == 'E':
            east += cval
        elif direction == 'W':
            east -= cval
        elif direction == 'N':
            north += cval
        elif direction == 'S':
            north -= cval
    # turn
    elif cdir == 'R':
        direction = directions[(directions.index(direction) + int(cval / 90)) % 4]
    elif cdir == 'L':
        direction = directions[(directions.index(direction) - int(cval / 90)) % 4]
    else:
        if cdir == 'E':
            east += cval
        elif cdir == 'W':
            east -= cval
        elif cdir == 'N':
            north += cval
        elif cdir == 'S':
            north -= cval
    print('instruction = ', instruction, ' / direction = ', direction, ', east = ', east, ', north = ', north)

print('result = ', abs(east) + abs(north))

