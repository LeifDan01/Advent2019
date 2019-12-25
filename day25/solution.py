from IntCodeComputer import IntCodeComputer

inputString = open("input.txt", "r").read()

computer = IntCodeComputer(inputString)
print(computer.status)

output = []

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
