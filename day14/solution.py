from math import ceil


inputString = open("test1.txt", "r").read()
# # 31  ore
# inputString = open("test2.txt", "r").read()
# # 165 ore
# inputString = open("test3.txt", "r").read()
# # 13312
# inputString = open("test4.txt", "r").read()
# # 180697
# inputString = open("test5.txt", "r").read()
# 2210736

# inputString = open("input.txt", "r").read()

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

need = rxs['FUEL'][1]
have = {}
AllOreMade = False
while not AllOreMade:
    AllOreMade = True
    oldFuel = need.copy()
    for entry in oldFuel:
        if entry != 'ORE':
            #WORK HERE
            AllOreMade = False
            needed = need.pop(entry)
            (get, rx) = rxs[entry]
            copies = ceil(needed / get)
            for item in rx:
                if item in need:
                    need[item] = need[item] + copies * rx[item]
                else:
                    need[item] = copies * rx[item]

print(need)
oreCount = 0
for item in need:
    print('need ' + str(need[item]) + ' of ' + item)
    print('using : ' + str(rxs[item]))
    (get, rx) = rxs[item]
    copies = ceil(need[item] / get)
    # print(str(copies) + ' of : ' + str(rx))
    print('cost : ' + str(copies * rx['ORE']))
    oreCount += copies * rx['ORE']
print(oreCount)
# 423895  High
