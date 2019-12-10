from math import gcd

inputString = open("input.txt", "r").read()

rows = inputString.split("\n")
height = len(rows)
width = len(rows[0])
print(str(height) + ' : ' + str(width))
things = set()
rowN = 0
for row in rows:
    colN = 0
    for item in row:
        if '#' == item:
            things.add((colN, rowN))
        colN += 1
    rowN += 1
    
bestThingCount = 0
bestPlace = None
for thing in things:
#     print('FOR ' + str(thing))
    otherThings = things.copy()
    otherThings.remove(thing)
    thingsDist = {}
    for oThing in otherThings:
        dist = abs(thing[0] - oThing[0]) + abs(thing[1] - oThing[1])
        thingsDist[oThing] = dist
    
    count = 0
    for oThing in sorted(thingsDist, key=thingsDist.get):
#         print('ADD ' + str(oThing))
        if oThing in otherThings:
            count += 1
        x = oThing[0] - thing[0]
        y = oThing[1] - thing[1]
        mygcd = gcd(x, y)
        x = x / mygcd
        y = y / mygcd
        position = thing
        while (position[0] >= 0 and position[0] <= width) and (position[1] >= 0 and position[1] <= height):
#             print('REMOVE ' + str(position))
            position = (position[0] + x, position[1] + y)
            otherThings.discard(position)
#     print('CAN SEE ' + str(count))
    if count > bestThingCount:
#         print(thing)
#         print(count)
        bestThingCount = count
        bestPlace = thing
    
print(bestPlace)
print(bestThingCount)
#269 (13, 17)
