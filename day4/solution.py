def isValid(number):
    maxVal = 0
    asStr = str(number)
    for c in asStr:
        if int(c) < maxVal:
            return False
        maxVal = int(c)
    for n in range(0, len(asStr) - 1):
        if asStr[n] == asStr[n+1]:
            if n == 0 or asStr[n] != asStr[n-1]:
                if (n + 2) == len(asStr) or asStr[n+1] != asStr[n+2]:
                    return True
    return False
print(isValid(123444))
print(isValid(111122))
count = 0
for n in range(248345, 746315):
    if isValid(n):
        count += 1
print(count)
