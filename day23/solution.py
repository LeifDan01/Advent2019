from IntCodeComputer import IntCodeComputer

inputString = open("input.txt", "r").read()

computers = {}
for n in range(50):
    computers[n] = IntCodeComputer(inputString)
    computers[n].addInput(n)

#NAT
natx = 0
naty = 0
lasty = 0
isIdle = 0
while True:
    isIdle += 1
    for computer in computers.values():
        if computer.numberOfOutput() >= 3:
            isIdle = 0
            dest = computer.getOutput()
            x = computer.getOutput()
            y = computer.getOutput()
            if dest == 255:
                natx = x
                naty = y
            else:
                computers[dest].addInput(x)
                computers[dest].addInput(y)
        if computer.status == 'waiting on input':
            computer.addInput(-1)
    if isIdle > 10:
        if lasty == naty:
            print('FOUND IT')
            print(lasty)
            quit()
        lasty = naty
        computers[0].addInput(natx)
        computers[0].addInput(naty)
