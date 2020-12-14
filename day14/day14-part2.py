import re
from itertools import count

data = open('day14/input.data').readlines()

maskRegex = re.compile('mask = (\w+)')
memSetRegex = re.compile('mem\[(\d+)\] = (\d+)')

memory = {}

DEBUG = False

def computeMemoryAddresses(addressWithFloatingBits):
    if not 'X' in addressWithFloatingBits:
        return [addressWithFloatingBits]
    else:
        addresses = list()
        xPos = next(i for i in count(0) if addressWithFloatingBits[i] == 'X')
        for p in computeMemoryAddresses(addressWithFloatingBits[:xPos] + '0' + addressWithFloatingBits[xPos+1:]):
            addresses.append(p)
        for p in computeMemoryAddresses(addressWithFloatingBits[:xPos] + '1' + addressWithFloatingBits[xPos+1:]):
            addresses.append(p)
        return addresses

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
        mem = '{0:b}'.format(int(groups[1])).zfill(36)
        if DEBUG:
            print(f'value = {mem}')
        maskedMem = ''
        for index, c in enumerate(mem):
            if currentMask[index] == '0':
                maskedMem += c
            else: 
                maskedMem += currentMask[index]
        if DEBUG:
            print(f'masked mem = {maskedMem}')

        for memPosition in computeMemoryAddresses(maskedMem):
            memory[memPosition] = int(groups[2])

if DEBUG:
    print(f'memory = {memory}')

accumulator = 0
for val in memory.values():
    accumulator += int(val)

print(f'result = {accumulator}')
