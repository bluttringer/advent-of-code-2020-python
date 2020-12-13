

data = open('day13/input.data').readlines()
time = int(data[0])

def idToInt(id):
    print('id = [', id, ']')
    return int(id.strip())

busIds = list(map(idToInt, [ busIds for busIds in data[1].strip().split(',') if busIds != 'x']))

print(time)
print(*busIds)
firstBusAvailableId = 0
minTimeToWait = 66536
for busId in busIds:
    print('busId =', busId)
    timeToWait = busId - time % busId
    print('timeToWait =', timeToWait)
    if (timeToWait < minTimeToWait):
        firstBusAvailableId = busId
        minTimeToWait = timeToWait

print('result = ', firstBusAvailableId * minTimeToWait)
