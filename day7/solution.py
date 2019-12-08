

# inputString = open("input.txt", "r").read()
# inputString = "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"
inputString = open("test.txt", "r").read()

opcodesOG = inputString.split(",")
# opcodes = list(map(int, opcodesOG))



class IntCodeComputer:
    def __init__(self, opcodes):
        self.state = 'created'
        self.position = 0
        self.opcodes = opcodes
        self.inputs = []
        self.outputs = []
        self.run()

    def addInput(self, value):
        self.inputs.append(value)
        self.run()

    def getOutput(self):
        if self.outputs:
            return self.outputs.pop()
        return None

    def parseInstruction(self, opcode):
        opcodeStr = str(opcode)
        modes = []
        if len(opcodeStr) < 2:
            return opcode, modes
        instruction = int(opcodeStr[-2:])
        modesStr = opcodeStr[0:-2]
        for n in modesStr:
            modes.append(int(n))
        return instruction, modes

    def getOpcodeValue(self, position, modes):
        addrValue = self.opcodes[position]
        if modes and 1 == modes.pop():
            return addrValue
        return self.opcodes[addrValue]

    def run(self):
        while True:
            instruction, modes = self.parseInstruction(self.opcodes[self.position])

            if 1 == instruction:
                op1 = self.getOpcodeValue(self.position + 1, modes)
                op2 = self.getOpcodeValue(self.position + 2, modes)
                dest = self.opcodes[self.position + 3]
                self.opcodes[dest] = op1 + op2
                self.position += 4
            elif 2 == instruction:
                op1 = self.getOpcodeValue(self.position + 1, modes)
                op2 = self.getOpcodeValue(self.position + 2, modes)
                dest = self.opcodes[self.position + 3]
                self.opcodes[dest] = op1 * op2
                self.position += 4
            elif 3 == instruction:
                if not self.inputs:
                    self.status = 'waiting on input'
                    return
                inputVal = self.inputs.pop()
                dest = self.opcodes[self.position + 1]
                print('Input: ' + str(inputVal))
                self.opcodes[dest] = inputVal
                self.position += 2
            elif 4 == instruction:
                output = self.getOpcodeValue(self.position + 1, modes)
                self.outputs.append(output)
                print('Output: ' + str(output))
                self.position += 2
            elif 5 == instruction:
                op1 = self.getOpcodeValue(self.position + 1, modes)
                op2 = self.getOpcodeValue(self.position + 2, modes)
                if op1 != 0:
                    self.position = op2
                else:
                    self.position += 3
            elif 6 == instruction:
                op1 = self.getOpcodeValue(self.position + 1, modes)
                op2 = self.getOpcodeValue(self.position + 2, modes)
                if op1 == 0:
                    self.position = op2
                else:
                    self.position += 3
            elif 7 == instruction:
                op1 = self.getOpcodeValue(self.position + 1, modes)
                op2 = self.getOpcodeValue(self.position + 2, modes)
                dest = self.opcodes[self.position + 3]
                if op1 < op2:
                    self.opcodes[dest] = 1
                else:
                    self.opcodes[dest] = 0
                self.position += 4
            elif 8 == instruction:
                op1 = self.getOpcodeValue(self.position + 1, modes)
                op2 = self.getOpcodeValue(self.position + 2, modes)
                dest = self.opcodes[self.position + 3]
                if op1 == op2:
                    self.opcodes[dest] = 1
                else:
                    self.opcodes[dest] = 0
                self.position += 4
            elif 99 == instruction:
                self.status = 'completed'
                return
            else:
                self.status = 'broke'
                return


computer = IntCodeComputer(list(map(int, opcodesOG)))
print(computer.status)
computer.addInput(5)
print(computer.status)
print(computer.getOutput())
