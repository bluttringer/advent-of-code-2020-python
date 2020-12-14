import re

data = open('day14/input.data').readlines()

maskRegex = re.compile('mask = (\w+)')
memSetRegex = re.compile('mem\[(\d+)\] = (\d+)')

memory = {}

DEBUG = False

currentMask = list()
for line in data:
    if DEBUG:
        print(f'currentMask = {currentMask}')
    if maskRegex.match(line):
        currentMask = maskRegex.search(line)[1]
        
    if memSetRegex.match(line):
        groups = memSetRegex.search(line)
        if DEBUG:
            print(f'mem[{groups[1]}] = {groups[2]}')
        value = '{0:b}'.format(int(groups[2])).zfill(36)
        if DEBUG:
            print(f'value = {value}')
        valueToSet = ''
        for index, c in enumerate(value):
            if (currentMask[index] != 'X'):
                valueToSet += currentMask[index]
            else:
                valueToSet +=c
        if DEBUG:
            print(f'value set = {valueToSet}')
        memory[groups[1]] = valueToSet

if DEBUG:
    print(f'memory = {memory}')

accumulator = 0
for val in memory.values():
    accumulator += int(val, 2)

print(f'result = {accumulator}')
