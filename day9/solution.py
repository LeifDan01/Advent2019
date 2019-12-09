from IntCodeComputer import IntCodeComputer

inputString = open("input.txt", "r").read()

# inputString = open("test.txt", "r").read()
# Day9 input run with 1 for validation and 2 for performance

# inputString = "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"
# Day5 999 if the input value is below 8, output 1000 if the input value is equal to 8, or output 1001 if the input value is greater than 8

# inputString = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
# Day9 outputs a copy of itself

# inputString = "1102,34915192,34915192,7,4,7,99,0"
# Day9 outputs a 16 digit number

# inputString = "104,1125899906842624,99"
# Day9 outputs number in middle

opcodesOG = inputString.split(",")
opcodes = {}
position = 0
for code in list(map(int, opcodesOG)):
    opcodes[position] = code
    position +=1


computer = IntCodeComputer(opcodes)
print(computer.status)
computer.addInput(2)
print(computer.status)
output = computer.getOutput()
while output != None:
    print(output)
    output = computer.getOutput()
