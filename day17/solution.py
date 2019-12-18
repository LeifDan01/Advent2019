from IntCodeComputer import IntCodeComputer

inputString = open("input.txt", "r").read()

computer = IntCodeComputer(inputString)
print(computer.status)

output = []
myPosition = (0,0)
while computer.status != 'completed':
    output = []
    while computer.hasOutput():
        value = computer.getOutput()
        if value > 255:
            print('FOUND IT: ' + str(value))
        else:
            output.append(chr(value))
    print(''.join(output))
    row = 0
    col = 0
    tracks = set()
    for item in output:
        if item == '.':
            col += 1
        elif item == '#':
            tracks.add((col, row))
            col += 1
        elif item == '\n':
            row += 1
            col = 0
        elif item == '^':
            myPosition = (col, row)
            col += 1

    usingCol = True
    canTurn = True
    while canTurn:
        oldPosition = myPosition
        # print(myPosition)
        x, y = myPosition
        if usingCol:
            direction = 1 if (x+1, y) in tracks else -1
            count = x
            while (count+direction, y) in tracks:
                count += direction
            myPosition = (count, y)
        else:
            direction = 1 if (x, y+1) in tracks else -1
            count = y
            while (x, count+direction) in tracks:
                count += direction
            myPosition = (x, count)
        x, y = myPosition
        usingCol = not usingCol
        if usingCol:
            canTurn = (x+1, y) in tracks or (x-1, y) in tracks
        else:
            canTurn = (x, y+1) in tracks or (x, y-1) in tracks

        move = (x - oldPosition[0], y - oldPosition[1])
        movement = move[0] if move[0] != 0 else move[1]
        print(movement)


    answer = input()
    for char in answer:
        value = ord(char)
        print(value)
        computer.addInput(value)
    value = ord('\n')
    print(value)
    computer.addInput(value)
    print(computer.status)

output = []
while computer.hasOutput():
    value = computer.getOutput()
    if value > 255:
        print('FOUND IT: ' + str(value))
    else:
        output.append(chr(value))
print(''.join(output))
# crossSections = set()
# for track in tracks:
#     x, y = track
#     if {(x-1,y),(x+1,y),(x,y-1),(x,y+1)}.issubset(tracks):
#         crossSections.add(track)
# print(crossSections)
#
# count = 0
# for track in crossSections:
#     x, y = track
#     count += x * y
# print(count)
#840 low
# 7328
# def getBoardColor(x, y):
#     tileType = screen[(x, y)] if (x,y) in screen else 0
#     if 0 == tileType:
#         # if (x,y) in pathTo:
#         #     return str(pathTo[(x,y)])[-1]
#         return ' '
#     elif 1 == tileType:
#         return '█'
#     elif 2 == tileType:
#         return '#'
#     elif 3 == tileType:
#         return 'D'
#     elif 4 == tileType:
#         return '*'
#     else:
#         if myPosition == (x, y):
#             return 'D'
#         return ' '
#
# computer = IntCodeComputer(inputString)
# myPosition = (0, 0)
# screen = {myPosition: 3}
# pathTo = {myPosition: 0}
# resetOnce = True
# while computer.status != 'completed':
#     if computer.status == 'waiting on input':
#         distance = pathTo[myPosition]
#         # print('current ' + str(distance))
#         # point = max(pathTo, key=pathTo.get)
#         # print('furthest is ' + str(point) + ' at a distance of: ' + str(pathTo[point]))
#
#         #north (1), south (2), west (3), and east (4)
#         if (myPosition[0]-1, myPosition[1]) not in screen:
#             nextPosition = (myPosition[0]-1, myPosition[1])
#             computer.addInput(4)
#         elif (myPosition[0], myPosition[1]-1) not in screen:
#             nextPosition = (myPosition[0], myPosition[1]-1)
#             computer.addInput(2)
#         elif (myPosition[0]+1, myPosition[1]) not in screen:
#             nextPosition = (myPosition[0]+1, myPosition[1])
#             computer.addInput(3)
#         elif (myPosition[0], myPosition[1]+1) not in screen:
#             nextPosition = (myPosition[0], myPosition[1]+1)
#             computer.addInput(1)
#         else:
#             options = {}
#             if (myPosition[0]-1, myPosition[1]) in pathTo:
#                 options['j'] = pathTo[(myPosition[0]-1, myPosition[1])]
#             if (myPosition[0], myPosition[1]-1) in pathTo:
#                 options['k'] = pathTo[(myPosition[0], myPosition[1]-1)]
#             if (myPosition[0]+1, myPosition[1]) in pathTo:
#                 options['l'] = pathTo[(myPosition[0]+1, myPosition[1])]
#             if (myPosition[0], myPosition[1]+1) in pathTo:
#                 options['i'] = pathTo[(myPosition[0], myPosition[1]+1)]
#             if options:
#                 key = min(options, key=options.get)
#             else:
#                 key = input('Next Direction? ') #north (1), south (2), west (3), and east (4)
#             if key == 'j':
#                 nextPosition = (myPosition[0]-1, myPosition[1])
#                 computer.addInput(4)
#             if key == 'k':
#                 nextPosition = (myPosition[0], myPosition[1]-1)
#                 computer.addInput(2)
#             if key == 'l':
#                 nextPosition = (myPosition[0]+1, myPosition[1])
#                 computer.addInput(3)
#             if key == 'i':
#                 nextPosition = (myPosition[0], myPosition[1]+1)
#                 computer.addInput(1)
#
#     while computer.hasOutput():
#         output = computer.getOutput()
#         # print(output)
#         if output == 0:
#             screen[nextPosition] = 2
#         if output == 1:
#             screen[myPosition] = 0
#             myPosition = nextPosition
#             screen[myPosition] = 3
#             if myPosition in pathTo:
#                 if pathTo[myPosition] > (distance + 1):
#                     pathTo[myPosition] = distance + 1
#             else:
#                 pathTo[myPosition] = distance + 1
#
#         if output == 2:
#             screen[nextPosition] = 4
#             screen[myPosition] = 0
#             myPosition = nextPosition
#             if resetOnce:
#                 resetOnce = False
#                 pathTo = {myPosition: 0}
#                 screen = {myPosition: 3}
#             else:
#                 computer.status = 'completed'
#
#     # print()
#     # print()
#     # print()
#     # print()
#     # print()
#     # print()
#     # minx = 1000000
#     # maxx = -1000000
#     # miny = 1000000
#     # maxy = -1000000
#     # for position in screen:
#     #     minx = min(minx, position[0])
#     #     maxx = max(maxx, position[0])
#     #     miny = min(miny, position[1])
#     #     maxy = max(maxy, position[1])
#     #
#     # for y in reversed(range(miny, maxy + 1)):
#     #     spots = []
#     #     for x in range(minx, maxx + 1):
#     #         spots.append(getBoardColor(x, y))
#     #     print (''.join(spots))
#
# print('current ' + str(distance))
# point = max(pathTo, key=pathTo.get)
# print('furthest is ' + str(point) + ' at a distance of: ' + str(pathTo[point]))
