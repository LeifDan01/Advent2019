

file = open("input.txt", "r").read()
wires = file.split("\n")
wire1 = "R8,U5,L5,D3".split(',') #lines[0].split(",")
wire2 = "U7,R6,D4,L4".split(',') #lines[1].split(',')

wire1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(',') #lines[0].split(",")
wire2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(',') #lines[1].split(',')

wire1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(',') #lines[0].split(",")
wire2 = "U62,R66,U55,R34,D71,R55,D58,R83".split(',') #lines[1].split(',')

wire1 = wires[0].split(",")
wire2 = wires[1].split(',')

line1points = {}
intersetion = {}
steps = 0
position = [0,0]
for move in wire1:
    # print(position)
    # print(steps)
    if move[0] == 'R':
        end = position[0] + int(move[1:])
        for x in range(1, int(move[1:])+1):
            steps += 1
            if not str(position[0] + x) + ',' + str(position[1]) in line1points:
                line1points[str(position[0] + x) + ',' + str(position[1])] = steps
                # print(str(position[0] + x) + ',' + str(position[1]))
                # print(steps)
        position[0] = end
    elif move[0] == 'L':
        end = position[0] - int(move[1:])
        for x in range(1, int(move[1:])+1):
            steps += 1
            if not str(position[0] - x) + ',' + str(position[1]) in line1points:
                line1points[str(position[0] - x) + ',' + str(position[1])] = steps
                # print(str(position[0] - x) + ',' + str(position[1]))
                # print(steps)
        position[0] = end
    elif move[0] == 'U':
        end = position[1] + int(move[1:])
        for y in range(1, int(move[1:])+1):
            steps += 1
            if not str(position[0]) + ',' + str(position[1] + y) in line1points:
                line1points[str(position[0]) + ',' + str(position[1] + y)] = steps
                # print(str(position[0]) + ',' + str(position[1] + y))
                # print(steps)
        position[1] = end
    elif move[0] == 'D':
        end = position[1] - int(move[1:])
        for y in range(1, int(move[1:])+1):
            steps += 1
            if not str(position[0]) + ',' + str(position[1] - y) in line1points:
                line1points[str(position[0]) + ',' + str(position[1] - y)] = steps
                # print(str(position[0]) + ',' + str(position[1] - y))
                # print(steps)
        position[1] = end

# print(position)
# print(steps)
# print(line1points)

steps = 0
position = [0,0]
for move in wire2:
    if move[0] == 'R':
        end = position[0] + int(move[1:])
        for x in range(1, int(move[1:])+1):
            steps += 1
            if str(position[0] + x) + ',' + str(position[1]) in line1points:
                if not str(position[0] + x) + ',' + str(position[1]) in intersetion:
                    print(str(position[0] + x) + ',' + str(position[1]))
                    print(line1points[str(position[0] + x) + ',' + str(position[1])])
                    print(str(steps))
                    intersetion[str(position[0] + x) + ',' + str(position[1])] = steps + line1points[str(position[0] + x) + ',' + str(position[1])]
        position[0] = end
    elif move[0] == 'L':
        end = position[0] - int(move[1:])
        for x in range(1, int(move[1:])+1):
            steps += 1
            if str(position[0] - x) + ',' + str(position[1]) in line1points:
                if not str(position[0] - x) + ',' + str(position[1]) in intersetion:
                    print(str(position[0] - x) + ',' + str(position[1]))
                    print(line1points[str(position[0] - x) + ',' + str(position[1])])
                    print(str(steps))
                    intersetion[str(position[0] - x) + ',' + str(position[1])] = steps + line1points[str(position[0] - x) + ',' + str(position[1])]
        position[0] = end
    elif move[0] == 'U':
        end = position[1] + int(move[1:])
        for y in range(1, int(move[1:])+1):
            steps += 1
            if str(position[0]) + ',' + str(position[1] + y) in line1points:
                if not str(position[0]) + ',' + str(position[1] + y) in intersetion:
                    print(str(position[0]) + ',' + str(position[1] + y))
                    print(line1points[str(position[0]) + ',' + str(position[1] + y)])
                    print(str(steps))
                    intersetion[str(position[0]) + ',' + str(position[1] + y)] = steps + line1points[str(position[0]) + ',' + str(position[1] + y)]
        position[1] = end
    elif move[0] == 'D':
        end = position[1] - int(move[1:])
        for y in range(1, int(move[1:])+1):
            steps += 1
            if str(position[0]) + ',' + str(position[1] - y) in line1points:
                if not str(position[0]) + ',' + str(position[1] - y) in intersetion:
                    print(str(position[0]) + ',' + str(position[1] - y))
                    print(line1points[str(position[0]) + ',' + str(position[1] - y)])
                    print(str(steps))
                    intersetion[str(position[0]) + ',' + str(position[1] - y)] = steps + line1points[str(position[0]) + ',' + str(position[1] - y)]
        position[1] = end

print(intersetion)

bestpoint = 1000000
for point in intersetion:
    value = intersetion[point]
    if value > 0 and value < bestpoint:
        bestpoint = value

print(bestpoint)

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
