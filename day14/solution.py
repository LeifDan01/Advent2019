from math import ceil


# inputString = open("test1.txt", "r").read()
# 31  ore
inputString = open("test2.txt", "r").read()
# 165 ore
inputString = open("test3.txt", "r").read()
# 13312
inputString = open("test4.txt", "r").read()
# 180697
inputString = open("test5.txt", "r").read()
# 2210736

# inputString = open("input.txt", "r").read()

def isOreMade(item):
    return 'ORE' in rxs[item][1]

rxs = {}

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

fuel = rxs['FUEL'][1]
AllOreMade = False
while not AllOreMade:
    AllOreMade = True
    oldFuel = fuel.copy()
    for entry in oldFuel:
        if not isOreMade(entry):
            AllOreMade = False
            needed = fuel.pop(entry)
            (get, rx) = rxs[entry]
            copies = ceil(needed / get)
            for item in rx:
                if item in fuel:
                    fuel[item] = fuel[item] + copies * rx[item]
                else:
                    fuel[item] = copies * rx[item]

print(fuel)
oreCount = 0
for item in fuel:
    print('need ' + str(fuel[item]) + ' of ' + item)
    print('using : ' + str(rxs[item]))
    (get, rx) = rxs[item]
    copies = ceil(fuel[item] / get)
    # print(str(copies) + ' of : ' + str(rx))
    print('cost : ' + str(copies * rx['ORE']))
    oreCount += copies * rx['ORE']
print(oreCount)
# 423895  High
