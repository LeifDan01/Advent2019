import threading
from datetime import datetime

# inputString = open("input.txt", "r").read()
inputString = open("input2.txt", "r").read()
# inputString = open("test4.txt", "r").read()
# 8
# inputString = open("test1.txt", "r").read()
# # # # #81
# # # # inputString = open("test2.txt", "r").read()
# # # # #86
# inputString = open("test3.txt", "r").read()
# #136

doors = {}          # 'A' : (x,y)
passages = set()     # (x,y)
keys = {}           # (x,y): 'a'
startpositions = [] 
row = 0
col = 0
for e in inputString:
    if e == '\n':
        row += 1
        col = 0
    elif e =='.':
        passages.add((col, row))
        col += 1
    elif e == '@':
        startpositions.append((col, row))
        passages.add((col, row))
        col += 1
    elif e.isupper():
        doors[e] = (col, row)
        col += 1
    elif e.islower():
        keys[(col, row)] = e
        col += 1
    else:
        col += 1

def findOptions(position, opened):
    options = {}        # (x,y) : 23
    distance = 0
    distanceTo = {position: distance}     # (x,y) : 23
    found = {position}
    while found:
        distance += 1
        checkAround = found
        found = set()
        for position in checkAround:
            x,y = position
            around = [(x,y+1), (x+1,y), (x,y-1), (x-1,y)]
            for check in around:
                if check not in distanceTo:
                    if check in passages or check in opened:
                            found.add(check)
                            distanceTo[check] = distance
                    elif check in keys and check not in options:
                        options[check] = distance
    return options
        
            #   positions,  opened, distance 
searchPaths = [(startpositions, set(), 0)]
best = 5000
def haveBetterRouteThan(positions, opened, distance):
    if distance >= best:
        return False
    for opositions, oopened, odistance in searchPaths:
        if positions[0] == opositions[0] and positions[1] == opositions[1] and positions[2] == opositions[2] and positions[3] == opositions[3] and odistance <= distance and opened.issubset(oopened):
            return True
    return False

while searchPaths:
    now = datetime.now()
    current_time = now. strftime("%H:%M:%S")
    print("Current Time =", current_time)
    print(len(searchPaths[0][1])/2)
    print(len(searchPaths))
    allPaths = False
    
    oldPaths = searchPaths
    searchPaths = []
    for positions, opened, distance in sorted(oldPaths, key = lambda x: x[2]):
        skip = distance >= best
        if not skip:
            for opositions, oopened, odistance in oldPaths:
                if positions[0] == opositions[0] and positions[1] == opositions[1] and positions[2] == opositions[2] and positions[3] == opositions[3] and odistance < distance and opened.issubset(oopened):
                    skip = True
                    break
        if not skip:
            options =  [] # [(positions, distance)] 
            for n in range(len(positions)):
                results = findOptions(positions[n], opened)
                for result in results:
                    tempp = positions.copy()
                    tempp[n] = result
                    options.append((tempp, results[result]))
                
            if not options:
                if distance < best:
                    best = distance
                    print('FOUND SOMETHING')
                    print(distance)
            else:
                for destinations, travel in sorted(options, key = lambda x : x[1]):
                    newdistance = distance + travel
                    myopened = opened.copy()
                    for destination in destinations:
                        if destination in keys:
                            key = keys[destination]
                            door = key.upper()
                            myopened.add(destination)
                            if door in doors:
                                myopened.add(doors[door])
                    #check if we have a better path
                    if not haveBetterRouteThan(destinations, myopened, newdistance):
                        searchPaths.append((destinations, myopened, newdistance))
