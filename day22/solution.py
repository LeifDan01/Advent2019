
inputString = open("input.txt", "r").read()
numberOfCards = 119315717514047
# numberOfCards = 10007
# card at 6417 is 2019

top = 0
increment = 1

# numberOfCards = 10
# inputString = open("test1.txt", "r").read()
# # #Result: 0 3 6 9 2 5 8 1 4 7
# inputString = open("test2.txt", "r").read()
#Result:  3 0 7 4 1 8 5 2 9 6
loops = 101741582076661
for n in range(1): #(101741582076661):
    lines = inputString.split('\n')
    for line in lines:
        if line == 'deal into new stack':
            increment = -1 * increment
            top = (top + increment + numberOfCards) % numberOfCards
        elif 'deal with increment ' in line:
            value = int(line.split('deal with increment ')[1])
            #WOKR HERE
            increment = (increment * pow(value, numberOfCards - 2, numberOfCards)) % numberOfCards
        elif 'cut ' in line:
            value = int(line.split('cut ')[1])
            top = (top + (increment * value) + numberOfCards) % numberOfCards


# print(deck[((direction * 2020) + top + numberOfCards) % numberOfCards])

print('offset: ' + str(top))
print('increment: ' + str(increment))
print((top + increment * 2020) % numberOfCards)
print()

top = top * (1 - pow(increment, loops, numberOfCards)) * pow(1 - increment, numberOfCards - 2, numberOfCards)
increment = pow(increment, loops, numberOfCards) % numberOfCards

print('offset: ' + str(top))
print('increment: ' + str(increment))
print((top + increment * 2020) % numberOfCards)
# for n in range(numberOfCards):
#     card =  (top + increment * n) % numberOfCards
#     print(card)


# print(deck[2019])
#3525 too low
#2243 low
#4705 low
#6417 yup
