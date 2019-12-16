from math import ceil


inputString = '12345678'
#
inputString = '03036732577212944063491565474664'
# 24176176  84462026
# inputString = '19617804207202209144916044189917'
# 73745418  78725270
# inputString = '69317163492948606335995924319873'
# 52432133  53553731


# inputString = open("input.txt", "r").read()
offset = int(inputString[0:7]) +1
# offset = 0
print(offset)
print(len(inputString))
inputString = (inputString * 10000)
print(len(inputString))
inputString = inputString[offset:]
print(len(inputString))

def getMult(iterN, digN):
    if digN < iterN:
        return 0
    position = ceil(abs((iterN - digN - 1)) / (iterN + 1)) % 4
    if position == 0:
        return 0
    elif position == 1:
        return 1
    elif position == 2:
        return 0
    elif position == 3:
        return -1

for i in range(0,1):
    digits = []
    for digStr in inputString:
        digits.append(int(digStr))
    nextV = []
    for iterN in range(0,len(inputString)):
        calc = 0
#         digN = 0
        for digit in digits:
            calc += digit #* getMult(iterN, digN)
#             digN += 1
        nextV.append(str(abs(calc) % 10))
    inputString = ''.join(nextV)
print(i+1)
print(inputString[0:8])
