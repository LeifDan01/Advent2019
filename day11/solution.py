from IntCodeComputer import IntCodeComputer

inputString = open("input.txt", "r").read()

opcodesOG = inputString.split(",")
opcodes = {}
position = 0
for code in list(map(int, opcodesOG)):
    opcodes[position] = code
    position +=1


computer = IntCodeComputer(opcodes)
print(computer.status)
board = {}
position = (0, 0)
direction = 0 # 0 Up, 1 Right, 2 Down, 3 Left
paintedCount = 0
board[position] = 1

def turnAndMove(value):
    global position, board, direction, paintedCount
    #0 Left, 1 Right
    direction += 1 if value else -1   
    direction = (direction + 4) % 4
    
    if direction == 0:
        position = (position[0], position[1]+1)
    elif direction == 1:
        position = (position[0]+1, position[1])
    elif direction == 2:
        position = (position[0], position[1]-1)
    elif direction == 3:
        position = (position[0]-1, position[1])

def getBoardColor(position):
    #0 Black (default), 1 White
    if position in board:
        return board[position]
    return 0

def paintPosition(inputValue):
    global position, board, direction, paintedCount
    if position not in board:
        paintedCount = paintedCount + 1
    board[position] = inputValue
    
while computer.status != 'completed':
    computer.addInput(getBoardColor(position))
    second = computer.getOutput()
    first = computer.getOutput()
    paintPosition(first)
    turnAndMove(second)
    
minx = 1000000
maxx = -1000000
miny = 1000000
maxy = -1000000
for position in board:
    minx = min(minx, position[0])
    maxx = max(maxx, position[0])
    miny = min(miny, position[1])
    maxy = max(maxy, position[1])
    
print(minx)
print(maxx)
print(miny)
print(maxy)
    
for x in range(minx, maxx + 1):
    spots = []
    for y in range(miny, maxy + 1):
        if getBoardColor((x, y)) == 1:
            spots.append('*')
        else:
            spots.append(' ')
    print (''.join(spots))
            
print(paintedCount)
#1709 too low
