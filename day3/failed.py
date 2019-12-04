

file = open("input.txt", "r").read()
wires = file.split("\n")
wire1 = "R8,U5,L5,D3".split(',') #lines[0].split(",")
wire2 = "U7,R6,D4,L4".split(',')#lines[1].split(',')

intersection = {}

position = [0,0]
for move in wire1:
    start = list(position)
    if move[0] == 'R':
        end = position[0] + int(move[1:])
        for x in range(position[0], end):
            intersection[str(x) + ',' + str(position[1])] = 1
        position[0] = end
    elif move[0] == 'L':
        end = position[0] - int(move[1:])
        for x in range(end, position[0]):
            intersection[str(x) + ',' + str(position[1])] = 1
        position[0] = end
    elif move[0] == 'U':
        end = position[1] + int(move[1:])
        for y in range(position[1], end):
            intersection[str(start[0]) + ',' + str(y)] = 1
        position[1] = end
    elif move[0] == 'D':
        wire1Lines.append([list(position), 'temp'])
        position[1] = position[1] - int(move[1:])
        wire1Lines[-1][1] = list(position)

print(intersection)


# # opcodes = "1,1,1,4,99,5,6,0,99".split(',')
# noun = -1
# verb = 0
# opcodes = map(int, opcodesOG)
# while 19690720 != opcodes[0]:
#     print(opcodes[0])
#     opcodes = map(int, opcodesOG)
#     noun += 1
#     if 100 == noun:
#         noun = 0
#         verb += 1
#         if verb == 100:
#             break
#     print('Noun: ' + str(noun) + '   Verb:' + str(verb))
#     opcodes[1] = noun
#     opcodes[2] = verb
#     position = 0
#     while 99 != opcodes[position]:
#         if 1 == opcodes[position]:
#             op1 = opcodes[int(opcodes[position + 1])]
#             op2 = opcodes[int(opcodes[position + 2])]
#             dest = int(opcodes[position + 3])
#             opcodes[dest] = int(op1) + int(op2)
#             position += 4
#         elif 2 == opcodes[position]:
#             op1 = opcodes[int(opcodes[position + 1])]
#             op2 = opcodes[int(opcodes[position + 2])]
#             dest = int(opcodes[position + 3])
#             opcodes[dest] = int(op1) * int(op2)
#             position += 4
#         else:
#             print("BROKE")
#             break
#
# print('\nAnswer:')
# print(position)
# print(opcodes)
# # 682685 low
