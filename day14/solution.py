from math import ceil


inputString = open("test1.txt", "r").read()
# 31  ore
# inputString = open("test2.txt", "r").read()
# # 165 ore
# inputString = open("test3.txt", "r").read()
# # 13312
# inputString = open("test4.txt", "r").read()
# # 180697
inputString = open("test5.txt", "r").read()
# 2210736

inputString = open("input.txt", "r").read()
# 423895  High
# 411154 high
# 399063 check

rxs = {}



oreCount = 0
fuelCount = 4215654
while oreCount <= 1000000000000:
    for entry in inputString.split('\n'):
        if not entry:
            break
        (inputs, output) = entry.split(' => ')
        rx = {}
        for input in inputs.split(', '):
            (iCount, iType) = input.split(' ')
            rx[iType] = int(iCount)

        (oCount, oType) = output.split(' ')
        rxs[oType] = (int(oCount), rx)

    fuelCount += 1
    fuel = rxs['FUEL'][1]
    for x in fuel.copy():
        fuel[x] = fuelCount * fuel[x]

    extras = {}
    AllOreMade = False
    while not AllOreMade:
        AllOreMade = True
        oldFuel = fuel.copy()
        for entry in oldFuel:
            if not isOreMade(entry):
                AllOreMade = False
                needed = fuel.pop(entry)
                (get, rx) = rxs[entry]
                if entry in extras:
                    have = extras[entry]
                    if have >= needed:
                        extras[entry] = have - needed
                        copies = 0
                    else:
                        copies = ceil((needed - have) / get)
                        extras[entry] = (copies * get) - (needed - have)
                else:
                    copies = ceil(needed / get)
                    extras[entry] = (copies * get) - needed
                for item in rx:
                    if item in fuel:
                        fuel[item] = fuel[item] + copies * rx[item]
                    else:
                        fuel[item] = copies * rx[item]

    oreCount = 0
    for item in fuel:
        (get, rx) = rxs[item]
        copies = ceil(fuel[item] / get)
        oreCount += copies * rx['ORE']
    # print(extras)
print(str(oreCount) + ' can produce ' + str(fuelCount))
