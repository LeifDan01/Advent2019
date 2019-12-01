import math

file = open("input.txt", "r").read()
cargo = 0
total = 0
for n in file.split("\n"):
    if n:
        cargo = math.floor(int(n)/3) - 2
        added = math.floor(int(cargo)/3) - 2
        extraFuel = 0
        while added > 0:
            extraFuel += added
            added = math.floor(int(added)/3) - 2
        print(extraFuel)
        total += extraFuel

#3390596
print(total + 3390596)
#5085852 high
#1695256 low
#1692428 low
