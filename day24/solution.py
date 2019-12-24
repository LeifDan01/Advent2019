
inputString = open("input.txt", "r").read()

# inputString = open("test.txt", "r").read()
# #Result: 2129920

life =  set()

row = 0
col = 0
maxcol = 0
maxrow = 0
for input in inputString:
    if input == '\n':
        maxcol = col
        maxrow += 1
        row += 1
        col = 0
    elif input == '#':
        life.add((col, row))
        col += 1
    else:
        col += 1

def hash(myset):
    score = 0
    for item in life:
        x, y = item
        score += 2 ** (x + (y * maxcol))
    return score

prevLife = set()

print(maxcol)
print(maxrow)

while True:
    nextLife = set()
    for y in range(maxrow):
        for x in range(maxcol):
            score = 0
            arounds = [(x, y+1), (x+1,y), (x,y-1), (x-1,y)]
            for around in arounds:
                if around in life:
                    score += 1
            if (x,y) in life: #currently bug
                if score == 1:
                    nextLife.add((x,y))
            else:
                if score == 1 or score == 2:
                    nextLife.add((x,y))
    life = nextLife
    score = hash(life)
    if score in prevLife:
        print(score)
        break
    else:
        prevLife.add(score)

# print(life)
