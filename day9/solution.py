from IntCodeComputer import IntCodeComputer

inputString = open("input.txt", "r").read()

# inputString = open("test.txt", "r").read()
# Day5 input 5 should get 8684145

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
computer.addInput(1)
print(computer.status)
output = computer.getOutput()
while output != None:
    print(output)
    output = computer.getOutput()

# bestResult = 0
# bestInputs = []
# for input1 in range(5,10):
#     for input2 in range(5,10):
#         for input3 in range(5,10):
#             for input4 in range(5,10):
#                 for input5 in range(5,10):
#                     unique = True
#                     for value in range(5,10):
#                         if value not in [input1, input2, input3, input4, input5]:
#                             unique = False
#                     # if [9,7,8,5,6] != [input1, input2, input3, input4, input5]:
#                     #     unique = False
#                     if unique:
#                         print([input1, input2, input3, input4, input5])
#                         computer1 = IntCodeComputer(opcodes)
#                         computer1.addInput(input1)
#                         computer2 = IntCodeComputer(opcodes)
#                         computer2.addInput(input2)
#                         computer3 = IntCodeComputer(opcodes)
#                         computer3.addInput(input3)
#                         computer4 = IntCodeComputer(opcodes)
#                         computer4.addInput(input4)
#                         computer5 = IntCodeComputer(opcodes)
#                         computer5.addInput(input5)
#                         computer1Input = 0
#                         status = 'starting'
#                         loopCount = 0
#                         while status != 'completed':
#                             loopCount += 1
#                             computer1.addInput(computer1Input)
#                             computer2.addInput(computer1.getOutput())
#                             computer3.addInput(computer2.getOutput())
#                             computer4.addInput(computer3.getOutput())
#                             computer5.addInput(computer4.getOutput())
#                             computer1Input = computer5.getOutput()
#                             status = computer5.status
#                         print('Loops: ' + str(loopCount))
#                         print(computer1Input)
#                         if computer1Input > bestResult:
#                             bestResult = computer1Input
#                             bestInputs = [input1, input2, input3, input4, input5]
# print('\nBest found are:')
# print(bestInputs)
# print(bestResult)
