

class IntCodeComputer:
    def __init__(self, inputString):
        self.state = 'created'
        self.position = 0
        self.relativeBase = 0

        self.opcodesOG = inputString.split(",")
        self.opcodes = {}
        index = 0
        for code in list(map(int, self.opcodesOG)):
            self.opcodes[index] = code
            index +=1
        self.backupopcodes = self.opcodes.copy()

        self.inputs = []
        self.outputs = []
        self.run()

    def addInput(self, value):
        self.inputs.append(value)
        self.run()

    def hasOutput(self):
        return self.outputs != []

    def getOutput(self):
        if self.outputs:
            value = self.outputs[0]
            del self.outputs[0]
            return value
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
        def readPosition(n):
            if n not in self.opcodes:
                self.opcodes[n] = 0
            return self.opcodes[n]
        addrValue = readPosition(position)
        if modes:
            mode = modes.pop()
            if 1 == mode:
                return addrValue
            if 2 == mode:
                return readPosition(addrValue + self.relativeBase)
        return readPosition(addrValue)

    def getOpcodeAddress(self, position, modes):
        def readPosition(n):
            if n not in self.opcodes:
                self.opcodes[n] = 0
            return self.opcodes[n]
        addrValue = readPosition(position)
        if modes:
            mode = modes.pop()
            if 1 == mode:
                print('BROKE on getOpcodeAddress with Mode==1')
                return 0
            if 2 == mode:
                return addrValue + self.relativeBase
        return addrValue

    def restart(self):
        self.state = 'created'
        self.position = 0
        self.relativeBase = 0
        self.opcodes = self.backupopcodes.copy() 
        self.inputs = []
        self.outputs = []
        self.run()
    
    def run(self):
        while True:
            instruction, modes = self.parseInstruction(self.opcodes[self.position])

            if 1 == instruction:
                op1 = self.getOpcodeValue(self.position + 1, modes)
                op2 = self.getOpcodeValue(self.position + 2, modes)
                dest = self.getOpcodeAddress(self.position + 3, modes)
                self.opcodes[dest] = op1 + op2
                self.position += 4
            elif 2 == instruction:
                op1 = self.getOpcodeValue(self.position + 1, modes)
                op2 = self.getOpcodeValue(self.position + 2, modes)
                dest = self.getOpcodeAddress(self.position + 3, modes)
                self.opcodes[dest] = op1 * op2
                self.position += 4
            elif 3 == instruction:
                if not self.inputs:
                    self.status = 'waiting on input'
                    return
                inputVal = self.inputs.pop()
                dest = self.getOpcodeAddress(self.position + 1, modes)
#                 print('Input: ' + str(inputVal))
                self.opcodes[dest] = inputVal
                self.position += 2
            elif 4 == instruction:
                output = self.getOpcodeValue(self.position + 1, modes)
                self.outputs.append(output)
#                 print('Output: ' + str(output))
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
                dest = self.getOpcodeAddress(self.position + 3, modes)
                if op1 < op2:
                    self.opcodes[dest] = 1
                else:
                    self.opcodes[dest] = 0
                self.position += 4
            elif 8 == instruction:
                op1 = self.getOpcodeValue(self.position + 1, modes)
                op2 = self.getOpcodeValue(self.position + 2, modes)
                dest = self.getOpcodeAddress(self.position + 3, modes)
                if op1 == op2:
                    self.opcodes[dest] = 1
                else:
                    self.opcodes[dest] = 0
                self.position += 4
            elif 9 == instruction:
                op1 = self.getOpcodeValue(self.position + 1, modes)
                self.relativeBase += op1
                self.position += 2
            elif 99 == instruction:
                self.status = 'completed'
                return
            else:
                print('Broke on:')
                print(self.opcodes[self.position])
                self.status = 'broke'
                return
