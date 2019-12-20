import threading
from datetime import datetime

inputString = open("input.txt", "r").read()

# inputString = open("test2.txt", "r").read()
# #26
# inputString = open("test3.txt", "r").read()
# #396

input = {} # { (x,y) : '#'}
firstrow = False
firstcol = False
lastrow = 0
lastcol = 0
row = 0
col = 0
for e in inputString:
    if e == '#':
        if not firstrow:
            firstrow = row
            firstcol = col
        lastrow = row
        lastcol = col
    if e == '\n':
        row += 1
        col = 0
    else:
        input[(col,row)] = e
        col += 1

passages = set()     # (x,y)
warp = {}           # (x,y): (x,y) must add both directions
warpinner = set()      # (x,y)
warpouter = set()      # (x,y)
charactersdone = set()  # {(x,y)}
warptemp = {}  # {'AB' : (x,y)}
start = (0,0)  # 'AA'
end = (0,0)    # 'ZZ'
for e in input:
    if input[e] =='.':
        passages.add(e)
    elif input[e].isupper() and e not in charactersdone:
        x, y = e
        lookaround = {(0,1),(1,0),(0,-1),(-1,0)}
        destination = False
        otherCharacter = False
        #must find paired character and POSSIBLE destination
        #check if other warp is done and wire it up
        for direction in lookaround:
            destTemp = (e[0] + direction[0], e[1] + direction[1])
            otherTemp = (e[0] - direction[0], e[1] - direction[1])
            if destTemp in input and input[destTemp] == '.' and input[otherTemp].isupper():
                destination = destTemp
                otherCharacter = otherTemp
                break

        if destination:
            charactersdone.add(e)
            charactersdone.add(otherCharacter)
            if e[0] < otherCharacter[0] or e[1] < otherCharacter[1]:
                pair = input[e] + input[otherCharacter]
            else:
                pair = input[otherCharacter] + input[e]
            if pair == 'AA':
                start = (destination[0], destination[1], 0)
            elif pair == 'ZZ':
                end = (destination[0], destination[1], 0)
            elif pair in warptemp:
                destination2 = warptemp[pair]
                warp[destination] = destination2
                warp[destination2] = destination
                if destination[0] <= firstcol or destination[0] >= lastcol or destination[1] <= firstrow or destination[1] >= lastrow:
                    warpouter.add(destination)
                else:
                    warpinner.add(destination)
                if destination2[0] <= firstcol or destination2[0] >= lastcol or destination2[1] <= firstrow or destination2[1] >= lastrow:
                    warpouter.add(destination2)
                else:
                    warpinner.add(destination2)

            else:
                warptemp[pair] = destination

print(str((firstcol, firstrow)))
print(str((lastcol, lastrow)))

print(len(passages))
print(start)
print(end)
print(warp)
print(warptemp)
print()
print()
print(warpinner)
print()
print(warpouter)
# quit()

loops = 0
distanceTo = {start: 0}     # (x,y,z) : 23
found = {start}
while found:
    loops += 1
    print(loops)
    checkAround = found
    found = set()
    for position in checkAround:
        distance = distanceTo[position] + 1
        x,y,z = position
        around = [(x,y+1,z), (x+1,y,z), (x,y-1,z), (x-1,y,z)]
        for check in around:
            check2d = (check[0], check[1])
            if check == end:
                print(checkAround)
                print('found it')
                print(distance)
                quit()
            if check2d in warp:
                destination2d = warp[check2d]
                #this is where we go in and out
                if check2d in warpinner:
                    newz = check[2] + 1
                elif check2d in warpouter:
                    newz = check[2] - 1
                else:
                    print('WARP ERROR')
                if newz >= 0:
                    destination = (destination2d[0], destination2d[1], newz)
                    if destination not in distanceTo or (distance + 1) < distanceTo[destination]:
                        found.add(destination)
                        distanceTo[destination] = distance + 1
            if check not in distanceTo or distance < distanceTo[check]:
                if check2d in passages:
                    found.add(check)
                    distanceTo[check] = distance
print()
print(distanceTo)
print()
print(distanceTo[end])

#5742 low

            #   positions,  opened, distance
# searchPaths = [(startpositions, set(), 0)]
# best = 5000
# def haveBetterRouteThan(positions, opened, distance):
#     if distance >= best:
#         return False
#     for opositions, oopened, odistance in searchPaths:
#         if positions[0] == opositions[0] and positions[1] == opositions[1] and positions[2] == opositions[2] and positions[3] == opositions[3] and odistance <= distance and opened.issubset(oopened):
#             return True
#     return False
#
# while searchPaths:
#     now = datetime.now()
#     current_time = now. strftime("%H:%M:%S")
#     print("Current Time =", current_time)
#     print(len(searchPaths[0][1])/2)
#     print(len(searchPaths))
#     allPaths = False
#
#     oldPaths = searchPaths
#     searchPaths = []
#     for positions, opened, distance in sorted(oldPaths, key = lambda x: x[2]):
#         skip = distance >= best
#         if not skip:
#             for opositions, oopened, odistance in oldPaths:
#                 if positions[0] == opositions[0] and positions[1] == opositions[1] and positions[2] == opositions[2] and positions[3] == opositions[3] and odistance < distance and opened.issubset(oopened):
#                     skip = True
#                     break
#         if not skip:
#             options =  [] # [(positions, distance)]
#             for n in range(len(positions)):
#                 results = findOptions(positions[n], opened)
#                 for result in results:
#                     tempp = positions.copy()
#                     tempp[n] = result
#                     options.append((tempp, results[result]))
#
#             if not options:
#                 if distance < best:
#                     best = distance
#                     print('FOUND SOMETHING')
#                     print(distance)
#             else:
#                 for destinations, travel in sorted(options, key = lambda x : x[1]):
#                     newdistance = distance + travel
#                     myopened = opened.copy()
#                     for destination in destinations:
#                         if destination in keys:
#                             key = keys[destination]
#                             door = key.upper()
#                             myopened.add(destination)
#                             if door in doors:
#                                 myopened.add(doors[door])
#                     #check if we have a better path
#                     if not haveBetterRouteThan(destinations, myopened, newdistance):
#                         searchPaths.append((destinations, myopened, newdistance))
