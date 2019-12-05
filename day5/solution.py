

file = open("input.txt", "r").read()

opcodesOG = file.split(",")
# opcodesOG = "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99".split(',')
opcodes = list(map(int, opcodesOG))
inputVal = 9

def parseInstruction(opcode):
    opcodeStr = str(opcode)
    modes = []
    if len(opcodeStr) < 2:
        return opcode, modes
    instruction = int(opcodeStr[-2:])
    modesStr = opcodeStr[0:-2]
    for n in modesStr:
        modes.append(int(n))
    return instruction, modes

def getOpcodeValue(opcodes, position, modes):
    addrValue = opcodes[position]
    if modes and 1 == modes.pop():
        return addrValue
    return opcodes[addrValue]

position = 0
while True:
    instruction, modes = parseInstruction(opcodes[position])
    
    if 1 == instruction:
        op1 = getOpcodeValue(opcodes, position + 1, modes)
        op2 = getOpcodeValue(opcodes, position + 2, modes)
        dest = opcodes[position + 3]
        opcodes[dest] = op1 + op2
        position += 4
    elif 2 == instruction:
        op1 = getOpcodeValue(opcodes, position + 1, modes)
        op2 = getOpcodeValue(opcodes, position + 2, modes)
        dest = opcodes[position + 3]
        opcodes[dest] = op1 * op2
        position += 4
    elif 3 == instruction:
        dest = opcodes[position + 1]
        print('Input: ' + str(inputVal))
        opcodes[dest] = inputVal
        position += 2
    elif 4 == instruction:
        output = getOpcodeValue(opcodes, position + 1, modes)
        print('Output: ' + str(output))
        position += 2
    elif 5 == instruction:
        op1 = getOpcodeValue(opcodes, position + 1, modes)
        op2 = getOpcodeValue(opcodes, position + 2, modes)
        if op1 != 0:
            position = op2
        else:
            position += 3
    elif 6 == instruction:
        op1 = getOpcodeValue(opcodes, position + 1, modes)
        op2 = getOpcodeValue(opcodes, position + 2, modes)
        if op1 == 0:
            position = op2
        else:
            position += 3
    elif 7 == instruction:
        op1 = getOpcodeValue(opcodes, position + 1, modes)
        op2 = getOpcodeValue(opcodes, position + 2, modes)
        dest = opcodes[position + 3]
        if op1 < op2:
            opcodes[dest] = 1
        else:
            opcodes[dest] = 0
        position += 4
    elif 8 == instruction:
        op1 = getOpcodeValue(opcodes, position + 1, modes)
        op2 = getOpcodeValue(opcodes, position + 2, modes)
        dest = opcodes[position + 3]
        if op1 == op2:
            opcodes[dest] = 1
        else:
            opcodes[dest] = 0
        position += 4
    elif 99 == instruction:
        break
    else:
        print("BROKE")
        break
