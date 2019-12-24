
inputString = open("input.txt", "r").read()
numberOfCards = 119315717514047
deck = {}

top = 0
direction = 1

# numberOfCards = 10
# inputString = open("test1.txt", "r").read()
# #Result: 0 3 6 9 2 5 8 1 4 7
# inputString = open("test2.txt", "r").read()
# #Result:  3 0 7 4 1 8 5 2 9 6

for n in range(numberOfCards):
    deck[n] = n

for n in range(101741582076661):
    lines = inputString.split('\n')
    for line in lines:
        if line == 'deal into new stack':
            direction = -1 * direction
            top = (top + direction + numberOfCards) % numberOfCards
        elif 'deal with increment ' in line:
            value = int(line.split('deal with increment ')[1])
            newdeck = {}
            for n in range(numberOfCards):
                newposition = ((n * value) + numberOfCards) % numberOfCards
                postion = ((direction * n) + top + numberOfCards) % numberOfCards
                newdeck[newposition] = deck[postion]
            deck = newdeck
            top = 0
            direction = 1
        elif 'cut ' in line:
            value = int(line.split('cut ')[1])
            top = (top + (direction * value) + numberOfCards) % numberOfCards


print(deck[((direction * 2020) + top + numberOfCards) % numberOfCards])

# for n in range(numberOfCards):
#     position = ((direction * n) + top + numberOfCards) % numberOfCards
#     # print(deck[position])
#     if 2019 == deck[position]:
#         print(n)


# print(deck[2019])
#3525 too low
#2243 low
#4705 low
#6417
