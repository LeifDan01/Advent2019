import threading


inputString = open("input.txt", "r").read()
# inputString = open("test1.txt", "r").read()
# # # #81
# # # inputString = open("test2.txt", "r").read()
# # # #86
inputString = open("test3.txt", "r").read()
# #132

doors = {}          # 'A' : (x,y)
passages = set()     # (x,y)
keys = {}           # (x,y): 'a'
myPosition = (0,0)
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
        myPosition = (col, row)
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
    distanceTo = {position: distance}     # (x, y) : 23
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

shortest = 3218
paths = {} # {'abc' : 23}
def exploreOption(path, totalDistance, position, opened):
    global shortest, paths
    key = keys[position]
    door = key.upper()
    opened.add(position)
    if door in doors:
        opened.add(doors[door])
    path += key
    # check if we have a better route to this state
    for opath in paths:
        isContained = True
        for e in path:
            if e not in opath:
                isContained = False
                break
        if isContained and path[-1] == opath[-1] and paths[opath] <= totalDistance:
            return
        
    paths[path] = totalDistance
    options = findOptions(position, opened)
    if not options:
        print(str(path) + ' takes: ' + str(totalDistance))
        shortest = totalDistance
    else:
        for option in options:
            distance = totalDistance + options[option]
            if distance < shortest:
                exploreOption(path, distance, option, opened.copy())
        

options = findOptions(myPosition, set())
print(options)
for option in options:
    print(option)
    exploreOption('', options[option], option, set())
    
#     threading.Thread(target=exploreOption, args=('', options[option], option, set())).start() 
# print(paths)
# 3222 high
# 3218 high