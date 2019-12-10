

file = open("input.txt", "r").read()

opcodesOG = file.split(",")
# opcodes = "1,1,1,4,99,5,6,0,99".split(',')
noun = -1
verb = 0
opcodes = map(int, opcodesOG)
while 19690720 != opcodes[0]:
    print(opcodes[0])
    opcodes = map(int, opcodesOG)
    noun += 1
    if 100 == noun:
        noun = 0
        verb += 1
        if verb == 100:
            break
    print('Noun: ' + str(noun) + '   Verb:' + str(verb))
    opcodes[1] = noun
    opcodes[2] = verb
    position = 0
    while 99 != opcodes[position]:
        if 1 == opcodes[position]:
            op1 = opcodes[int(opcodes[position + 1])]
            op2 = opcodes[int(opcodes[position + 2])]
            dest = int(opcodes[position + 3])
            opcodes[dest] = int(op1) + int(op2)
            position += 4
        elif 2 == opcodes[position]:
            op1 = opcodes[int(opcodes[position + 1])]
            op2 = opcodes[int(opcodes[position + 2])]
            dest = int(opcodes[position + 3])
            opcodes[dest] = int(op1) * int(op2)
            position += 4
        else:
            print("BROKE")
            break

print('\nAnswer:')
print(position)
print(opcodes)
# 682685 low
