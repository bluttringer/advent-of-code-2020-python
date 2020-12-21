import re

DEBUG = True
LOG_LIMIT = 1

data = open('day15/input.data').readlines()

numbers = [int(c) for c in data[0].split(',')]

if DEBUG:
    print(f'numbers = {numbers}')

numbersSpokenStore = {}
for i, number in enumerate(numbers):
    if i == len(numbers) - 1:
        break
    # (x, y) : last turn number, number of the turn before the last turn number
    numbersSpokenStore[number] = (i+1, 0)

turn = len(numbers) + 1
lastSpokenNumber = numbers[-1]
while turn <= 30000000:
    if turn < LOG_LIMIT:
        print('------------------------')
        print(f'turn = {turn}')
        print(f'lastSpokenNumber = {lastSpokenNumber}')
    if lastSpokenNumber in numbersSpokenStore:
        lastTurn, previousTurn = numbersSpokenStore[lastSpokenNumber]
        spokenNumber = lastTurn - previousTurn
        if turn < LOG_LIMIT:
            print(f'-> {lastSpokenNumber} already said, I say {spokenNumber}')
    else:
        spokenNumber = 0
        if turn < LOG_LIMIT:
            print(f'-> {lastSpokenNumber} never said, I say {spokenNumber}')
        numbersSpokenStore[lastSpokenNumber] = (turn-1, 0)
    
    # update the numbersSpokenStore
    if spokenNumber in numbersSpokenStore:
        l, p = numbersSpokenStore[spokenNumber]
        numbersSpokenStore[spokenNumber] = (turn, l)
    
    if turn < LOG_LIMIT:
        print(f'updated numbersSpokenStore = {numbersSpokenStore}')

    lastSpokenNumber = spokenNumber
    turn += 1

print(f'turn = {turn}')
print(f'result = {lastSpokenNumber}')
