from IntCodeComputer import IntCodeComputer

inputString = open("input.txt", "r").read()
ballPosition = (20, 5)
def getBoardColor(x, y):
    global position, ballPosition
    tileType = screen[(x, y)]
    if 0 == tileType:
        return ' '
    elif 1 == tileType:
        return '█'
    elif 2 == tileType:
        return '#'
    elif 3 == tileType:
        position = x
        return '='
    elif 4 == tileType:
        ballPosition = (x, y)
        return '*'
    else:
        print('Got an undefined space')
        return ' '
    
placesToBe = [(22, 3)]
won = False

while not won:
    myPlacesToBe = placesToBe.copy()
    computer = IntCodeComputer(inputString)
    screen = {}
    score = 0
    move = 0
    position = 20
    nextPosition = (0, 0)
    while computer.status != 'completed':
        print(str(score))
        if computer.status == 'waiting on input':
            
            move += 1
            key = 'k'
            if True:
                if position > ballPosition[0]:
                    print('j')
                    key = 'j'
                elif position < ballPosition[0]:
                    print('l')
                    key = 'l'
            elif nextPosition:
                if move > nextPosition[1]:
                    if myPlacesToBe:
                        nextPosition = myPlacesToBe[0]
                        del myPlacesToBe[0]
                        print('Next move to x = ' + str(nextPosition[0]) + ' by move: ' + str(nextPosition[1]))
                    
                if nextPosition[0] > position:
                    print('l')
                    key = 'l'
                elif nextPosition[0] < position:
                    print('j')
                    key = 'j'
                else:
                    print('k')
            else:
#                 key = input("move joystick: ")
                pass
            
            if key == 'j':
                computer.addInput(-1)
            if key == 'k':
                computer.addInput(0)
            if key == 'l':
                computer.addInput(1)
        while computer.hasOutput():
            x = computer.getOutput()
            y = computer.getOutput()
            tileType = computer.getOutput()
            if (-1,0) == (x, y):
                score = tileType
            else:
                screen[(x,y)] = tileType
        
        print()
        print()
        print()
        print()
        print()
        print()      
        minx = 1000000
        maxx = -1000000
        miny = 1000000
        maxy = -1000000
        for position in screen:
            minx = min(minx, position[0])
            maxx = max(maxx, position[0])
            miny = min(miny, position[1])
            maxy = max(maxy, position[1])
             
        for y in range(miny, maxy + 1):
            spots = []
            for x in range(minx, maxx + 1):
                spots.append(getBoardColor(x, y))
            print (''.join(spots))
            
        if ballPosition[1] == 21:
            if ballPosition[0] == position:
                placesToBe.append((ballPosition[0], move))
            if ballPosition[0] == position - 1:
                placesToBe.append((ballPosition[0], move))
            if ballPosition[0] == position + 1:
                placesToBe.append((ballPosition[0], move))
            
    
    count = 0
    for tile in screen:
        if screen[tile] == 2:
            count += 1
        if screen[tile] == 3:
            position = tile[0]
            print("final location: " + str(position) + ' at move: ' + str(move))
        if screen[tile] == 4:
            placesToBe.append((tile[0], move))
            print(placesToBe)
          
    temp = input('Ended Here')  
    if count == 0:
        won = True
    
print(score)
# board = {}
# position = (0, 0)
# direction = 0 # 0 Up, 1 Right, 2 Down, 3 Left
# paintedCount = 0
# board[position] = 1
# 
# def turnAndMove(value):
#     global position, direction
#     #0 Left, 1 Right
#     direction += 1 if value else -1   
#     direction = (direction + 4) % 4
#     
#     if direction == 0:
#         position = (position[0], position[1]+1)
#     elif direction == 1:
#         position = (position[0]+1, position[1])
#     elif direction == 2:
#         position = (position[0], position[1]-1)
#     elif direction == 3:
#         position = (position[0]-1, position[1])
# 
# 
# def paintPosition(value):
#     global board, paintedCount
#     if position not in board:
#         paintedCount = paintedCount + 1
#     board[position] = value
#     
# def getBoardColor(position):
#     #0 Black (default), 1 White
#     if position in board:
#         return board[position]
#     return 0
# 
# while computer.status != 'completed':
#     computer.addInput(getBoardColor(position))
#     paintPosition(computer.getOutput())
#     turnAndMove(computer.getOutput())
#     

#             
# print(paintedCount)
# #1709 too low
