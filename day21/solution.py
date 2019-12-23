from IntCodeComputer import IntCodeComputer

inputString = open("input.txt", "r").read()

computer = IntCodeComputer(inputString)
print(computer.status)

output = []
operations = ['NOT ', 'AND ', 'OR ']
firstRegs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'T', 'J']
secondRegs = [' T', ' J']
inputValues = [
    'OR F J',
    'OR I J',
    'OR F T',
    'AND G T',
    'OR E T',
    'AND J T',
    'OR C T', # END c
    'NOT D J',
    'OR J T',
    'NOT T J', # if T is False then doesn't matter SO ASSUME T TRUE SO NOW J IS False
    'OR B J',
    'OR E J',
    'AND J T',
    'AND A T',
    'NOT T J',
    'RUN']

inputValues = [
    'NOT F J',
    'OR E J',
    'OR H J',
    'AND D J',
    'NOT C T',
    'AND T J',
    'NOT D T',
    'OR B T',
    'OR E T',
    'NOT T T',
    'OR T J',
    'NOT A T',
    'OR T J',
    'RUN']

while computer.status != 'completed':
    output = []
    while computer.hasOutput():
        value = computer.getOutput()
        if value > 255:
            print('FOUND IT: ' + str(value))
            quit()
        else:
            output.append(chr(value))
    print(''.join(output))

    if inputValues:
        answer = inputValues[0]
        print(answer)
        del inputValues[0]
    else:
        answer = input()
    for char in answer:
        value = ord(char)
        computer.addInput(value)
    value = ord('\n')
    computer.addInput(value)
    print(computer.status)

while computer.hasOutput():
    value = computer.getOutput()
    if value > 255:
        print('FOUND IT: ' + str(value))
        quit()
    else:
        output.append(chr(value))
print(''.join(output))
