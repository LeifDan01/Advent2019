from math import gcd, atan2

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

#destroy asteroids
thing = bestPlace
otherThings = things.copy()
otherThings.remove(thing)
pi = atan2(0, -1)
thingAnglesDist = {}
for oThing in otherThings:
    x = oThing[0] - thing[0]
    y = thing[1] - oThing[1]
    angle = atan2(x, y)
    if angle < 0:
        angle += 2*pi
    thingAnglesDist[oThing] = (angle, abs(x) + abs(y))

angle = -.0000001
count = 0
while count < 200 and thingAnglesDist:
    bestMatches = []
    bestAngle = 7
    for othing in thingAnglesDist:
        if thingAnglesDist[othing][0] > angle:
            if thingAnglesDist[othing][0] == bestAngle:
                bestMatches.append(othing)
            elif thingAnglesDist[othing][0] < bestAngle:
                bestAngle = thingAnglesDist[othing][0]
                bestMatches = [othing]
    if not bestMatches:
        angle = -.000001
    else:
        angle = bestAngle + .00001
        best = None
        distance = 1000
        for othing in bestMatches:
            if thingAnglesDist[othing][1] < distance:
                distance = thingAnglesDist[othing][1]
                best = othing
        count += 1
        print(str(count) + ' : ' + str(best) + '   ' + str(thingAnglesDist[best]))
        del thingAnglesDist[best]
