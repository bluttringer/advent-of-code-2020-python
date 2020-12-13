

data = open('day13/input.data').readlines()
time = int(data[0])

busIds = data[1].split(',')
busIdsLength = len(busIds)

print(time)
print(*busIds)

timestamp = 0
#timestamp=0
DEBUG = False
timeToAdd = 1
lastMatchingTimestampCount = 0

timeToAdd = 1
for index, busId in enumerate(busIds):
    print('timeToAdd :', timeToAdd)
    if busId != 'x':
        while (timestamp + index) % int(busId) != 0:
            timestamp += timeToAdd
        timeToAdd *= int(busId)

print('result = ', timestamp)
        
