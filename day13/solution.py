from IntCodeComputer import IntCodeComputer

inputString = open("input.txt", "r").read()

computer = IntCodeComputer(inputString)
print(computer.status)
screen = {}
score = 0
while computer.hasOutput():
    x = computer.getOutput()
    y = computer.getOutput()
    tileType = computer.getOutput()
    print('(' + str(x) + ', ' + str(y) + ') = ' + str(tileType))
    if (-1,0) == (x, y):
        score = tileType
    else:
        screen[(x,y)] = tileType

print('got outputs')
print(str(len(screen)))
print(screen)
count = 0
for tile in screen:
    if screen[tile] == 2:
        count += 1
        
print(computer.status)
print(count)
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
# minx = 1000000
# maxx = -1000000
# miny = 1000000
# maxy = -1000000
# for position in board:
#     minx = min(minx, position[0])
#     maxx = max(maxx, position[0])
#     miny = min(miny, position[1])
#     maxy = max(maxy, position[1])
#     
# print(minx)
# print(maxx)
# print(miny)
# print(maxy)
#     
# for y in reversed(range(miny, maxy + 1)):
#     spots = []
#     for x in range(minx, maxx + 1):
#         if getBoardColor((x, y)) == 1:
#             spots.append('█')
#         else:
#             spots.append(' ')
#     print (''.join(spots))
#             
# print(paintedCount)
# #1709 too low
