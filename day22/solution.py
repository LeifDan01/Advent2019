
inputString = open("input.txt", "r").read()
numberOfCards = 10007 # 119315717514047
deck = {}

top = 0
direction = 1
offset = 1

numberOfCards = 10
inputString = open("test1.txt", "r").read()
# #Result: 0 3 6 9 2 5 8 1 4 7
inputString = open("test2.txt", "r").read()
#Result:  3 0 7 4 1 8 5 2 9 6

for n in range(numberOfCards):
    deck[n] = n

for n in range(1): #(101741582076661):
    lines = inputString.split('\n')
    for line in lines:
        if line == 'deal into new stack':
            direction = -1 * direction
            top = (top + direction * offset  + numberOfCards) % numberOfCards
        elif 'deal with increment ' in line:
            value = int(line.split('deal with increment ')[1])
            #WOKR HERE
            offset = value * offset
            #try to reduce offset based on numberOfCards
        elif 'cut ' in line:
            value = int(line.split('cut ')[1])
            top = (top + (direction * value * offset) + numberOfCards) % numberOfCards


# print(deck[((direction * 2020) + top + numberOfCards) % numberOfCards])

print(top)
print(direction)
print(offset)
for n in range(numberOfCards):
    m = 0
    while 0 != (((direction * n) + top + numberOfCards) % numberOfCards + m * numberOfCards) % offset:
        m +=1
    card =  (((direction * n) + top + numberOfCards) % numberOfCards + m * numberOfCards) / offset
    print(card)


# print(deck[2019])
#3525 too low
#2243 low
#4705 low
#6417 yup
