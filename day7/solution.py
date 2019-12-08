from IntCodeComputer import IntCodeComputer

inputString = open("input.txt", "r").read()
# inputString = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"
# inputString = "3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"
# inputString = open("test.txt", "r").read()

opcodesOG = inputString.split(",")
opcodes = list(map(int, opcodesOG))

bestResult = 0
bestInputs = []
for input1 in range(5,10):
    for input2 in range(5,10):
        for input3 in range(5,10):
            for input4 in range(5,10):
                for input5 in range(5,10):
                    unique = True
                    for value in range(5,10):
                        if value not in [input1, input2, input3, input4, input5]:
                            unique = False
                    # if [9,7,8,5,6] != [input1, input2, input3, input4, input5]:
                    #     unique = False
                    if unique:
                        print([input1, input2, input3, input4, input5])
                        computer1 = IntCodeComputer(opcodes)
                        computer1.addInput(input1)
                        computer2 = IntCodeComputer(opcodes)
                        computer2.addInput(input2)
                        computer3 = IntCodeComputer(opcodes)
                        computer3.addInput(input3)
                        computer4 = IntCodeComputer(opcodes)
                        computer4.addInput(input4)
                        computer5 = IntCodeComputer(opcodes)
                        computer5.addInput(input5)
                        computer1Input = 0
                        status = 'starting'
                        loopCount = 0
                        while status != 'completed':
                            loopCount += 1
                            computer1.addInput(computer1Input)
                            computer2.addInput(computer1.getOutput())
                            computer3.addInput(computer2.getOutput())
                            computer4.addInput(computer3.getOutput())
                            computer5.addInput(computer4.getOutput())
                            computer1Input = computer5.getOutput()
                            status = computer5.status
                        print('Loops: ' + str(loopCount))
                        print(computer1Input)
                        if computer1Input > bestResult:
                            bestResult = computer1Input
                            bestInputs = [input1, input2, input3, input4, input5]
print('\nBest found are:')
print(bestInputs)
print(bestResult)
