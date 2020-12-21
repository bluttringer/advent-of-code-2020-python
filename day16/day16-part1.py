import re

DEBUG = False
DEBUG_COMPUTE = False


fieldRuleRegex = re.compile('(?P<name>.*): (?P<r1>\d+-\d+) or (?P<r2>\d+-\d+)')

fieldRules = {}
invalidValues = []
nearByTickets = []
yourTicket = []
    
def parseRule(line):
    rules = fieldRuleRegex.search(line).groupdict()
    rule1 = tuple([ int(r) for r in rules['r1'].split('-') ])
    rule2 = tuple([ int(r) for r in rules['r2'].split('-') ])
    return {rules['name'] : [rule1, rule2]}

def isValueCorrect(value, rule):
    if DEBUG:
        print(f'testing {value} against {rule}')
    oneAtLeastIsOk = False
    for condition in rule:
        if DEBUG:
            print(f'condition = {condition}')
        if value >= condition[0] and value <= condition[1]:
            oneAtLeastIsOk = True
            break
    if DEBUG:
        if not oneAtLeastIsOk:
            print(f'invalid value = {value}')
    return oneAtLeastIsOk

def areValuesCorrect(values, rule):
    if DEBUG:
        print(f'areValuesCorrect : {values} / {rule}')
    return len([ value for value in values if not isValueCorrect(value, rule)]) == 0

def sumInvalidValues(ticket, rules):
    sumInvalidValues = 0
    for fieldValue in ticket:
        sumInvalidValues += fieldValue
        # check value against all rules
        # if value is not valid for at least one rule, add it to the sum
        for conditions in rules.values():
            if isValueCorrect(fieldValue, conditions):
                sumInvalidValues -= fieldValue
                break
    return sumInvalidValues

def initialize(lines):
    nextLineIsYourTicket = False
    nextLineIsNearbyTicket = False
    for line in lines:
        if fieldRuleRegex.match(line):
            fieldRules.update(parseRule(line))

        if nextLineIsNearbyTicket:
            nearByTickets.append([ int(field) for field in line.split(',') ])
        elif nextLineIsYourTicket:
            print(f'your ticket = {line}')
            yourTicket.extend([ int(field) for field in line.split(',')])
            print(f'your ticket as a list = {yourTicket}')
            nextLineIsYourTicket = False

        if line.startswith('your ticket:'):
            nextLineIsYourTicket = True

        if line.startswith('nearby tickets:'):
            nextLineIsNearbyTicket = True

    if DEBUG:
        print(f'fieldRules = {fieldRules}')
        print(f'nearby tickets = {nearByTickets}')

def computeValidFields(tickets):
    # trouver pour chaque champs de chaque ticket quelle regle peut s'appliquer
    # itérer avec les tickets suivants pour éliminer ceux qui ne deviennent plus possible
    possibilities = { i: set(fieldRules.keys()) for i in range(len(fieldRules)) }
    print(f'possibilities = {possibilities}')
    for ticket in tickets:
        if DEBUG_COMPUTE:
            print(f'ticket = {ticket}')
        for i, fieldValue in enumerate(ticket):
            if DEBUG_COMPUTE:
                print(f' [{i}] fieldValue = {fieldValue}')
            for name in fieldRules.keys():
                if DEBUG_COMPUTE:
                    print(f'  field name: {name}, rule = {fieldRules[name]}')
                if not isValueCorrect(fieldValue, fieldRules[name]):
                    if DEBUG_COMPUTE:
                        print(f'  not match')
                    possibilities[i].discard(name)
                if DEBUG_COMPUTE:
                    print(f'  possibilities = {possibilities}')

    for i in sorted(possibilities, key=lambda k: len(possibilities[k])):
        this_field = next(iter(possibilities[i]))
        for j in possibilities:
            if i != j:
                possibilities[j].discard(this_field)

    return possibilities
            

def go(filename):
    initialize(open(filename).readlines())

    errorRate = 0
    validTickets = []
    for ticket in nearByTickets:
        errorValue = sumInvalidValues(ticket, fieldRules)
        if errorValue == 0:
            validTickets.append(ticket)
        errorRate += errorValue
        if DEBUG:
            print(f'ticket: {ticket}, errorRate: {errorRate}')

    print(f'error rate = {errorRate}')
    if DEBUG:
        print(f'valid tickets: {validTickets}')

    # Compute valid field order
    validTickets.append(yourTicket)
    validFields = computeValidFields(validTickets)

    print(f'valid fields = {validFields}')

    print(f'your ticket = {yourTicket}')

    result = 1
    for i in validFields:
        fieldName = validFields[i].pop()
        if fieldName.startswith('departure'):
            print(f'field name: {fieldName}, value: {yourTicket[i]}')
            result *= yourTicket[i]

    print(f'result = {result}')

if __name__ == '__main__':
    go('input.data')