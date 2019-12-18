import threading


inputString = open("input.txt", "r").read()
inputString = open("test1.txt", "r").read()
# #81
# inputString = open("test2.txt", "r").read()
# #86
# inputString = open("test3.txt", "r").read()
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

def findOptions(position, passages, keys):
    options = {}        # (x,y) : 23
    distance = 0
    distanceTo = {position: distance}     # (x, y) : 23
    found = [position]
    while found:
        distance += 1
        checkAround = found
        found = []
        for position in checkAround:
            x,y = position
            around = [(x,y+1), (x+1,y), (x,y-1), (x-1,y)]
            for check in around:
                if check in keys:
                    if check not in options:
                        options[check] = distance
                if check not in distanceTo and check in passages:
                    found.append(check)
                    distanceTo[check] = distance
    return options

def moveTo(position, passages, keys, doors):
    key = keys[position]
    del keys[position]
    door = key.upper()
    passages.add(position)
    if door in doors:
        passages.add(doors[door])
        del doors[door]  # can possibly remove
    return key
        
paths = {}          # 'adefh' : 23
shortest = 10000000
def exploreOption(path, totalDistance, option, passages, keys, doors):
    global paths, shortest
    position = option
    passages = passages.copy()
    keys = keys.copy()
    doors = doors.copy()
    path += moveTo(position, passages, keys, doors)
    options = findOptions(position, passages, keys)
    if not options:
        print(path + ' takes: ' + str(totalDistance))
        shortest = totalDistance
        paths[path] = totalDistance
    else:
        for option in options:
            if (totalDistance + options[option]) < shortest:
#                 threading.Thread(target=exploreOption, args=(path, totalDistance + options[option], option, passages, keys, doors)).start()
                exploreOption(path, totalDistance + options[option], option, passages, keys, doors)
        

options = findOptions(myPosition, passages, keys)
print(options)
for option in options:
    print(option)
#     threading.Thread(target=exploreOption, args=('', options[option], option, passages, keys, doors)).start() 
    exploreOption('', options[option], option, passages, keys, doors)
print(paths)
# 3222 high