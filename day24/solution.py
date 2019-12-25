
inputString = open("input.txt", "r").read()

# inputString = open("test1.txt", "r").read()
# #Result: 99 after 10 with -5 to 5 depth

life =  set()

row = 0
col = 0
maxx = 0
maxy = 0
for input in inputString:
    if input == '\n':
        maxx = col
        maxy += 1
        row += 1
        col = 0
    elif input == '#':
        life.add((col, row, 0))
        col += 1
    else:
        col += 1
print(len(life))
midx = int((maxx - 1) / 2)
midy = int((maxy - 1) / 2)
bottom = 0
top = 0
midpoint = (midx, midy)

for _ in range(200):
    print()
    print()
    print()
    # for z in range(bottom, top+1):
    #     print()
    #     print('on depth :' + str(z))
    #     for y in range(0, 5):
    #         line = ''
    #         for x in range(0,5):
    #             if (x, y, z) in life:
    #                 line += '#'
    #             else:
    #                 line += '.'
    #         print(line)
    nextLife = set()
    for z in range(bottom-1, top+2):
        for y in range(maxy):
            for x in range(maxx):
                if (x,y) != midpoint:
                    realarounds = []
                    arounds = [(x, y+1), (x+1,y), (x,y-1), (x-1,y)]
                    for around in arounds:
                        nextx, nexty = around
                        if around == midpoint:
                            if x > midx:
                                for ys in range(maxy):
                                    realarounds.append((maxx-1, ys, z - 1))
                            elif x < midx:
                                for ys in range(maxy):
                                    realarounds.append((0, ys, z - 1))
                            elif y > midy:
                                for xs in range(maxx):
                                    realarounds.append((xs, maxy - 1, z - 1))
                            elif y < midy:
                                for xs in range(maxx):
                                    realarounds.append((xs, 0, z - 1))
                        elif nextx >= maxx:
                            realarounds.append((midx + 1, midy, z + 1))
                        elif nextx < 0:
                            realarounds.append((midx - 1, midy, z + 1))
                        elif nexty >= maxy:
                            realarounds.append((midx, midy + 1, z + 1))
                        elif nexty < 0:
                            realarounds.append((midx, midy - 1, z + 1))
                        else:
                            realarounds.append((nextx, nexty, z))
                    if (x,y,z) == (4,0,-1):
                        print(realarounds)
                    score = 0
                    for around in realarounds:
                        if around in life:
                            score += 1
                    if (x,y,z) in life: #currently bug
                        if score == 1:
                            bottom = min(bottom, z - 1)
                            top = max(top, z + 1)
                            nextLife.add((x,y,z))
                    else:
                        if score == 1 or score == 2:
                            bottom = min(bottom, z - 1)
                            top = max(top, z + 1)
                            nextLife.add((x,y,z))
    life = nextLife

# print()
# print()
# print()
# for z in range(bottom, top+1):
#     print()
#     print('on depth :' + str(z))
#     for y in range(0, 5):
#         line = ''
#         for x in range(0,5):
#             if (x, y, z) in life:
#                 line += '#'
#             else:
#                 line += '.'
#         print(line)

print(bottom)
print(top)
print(len(life))
