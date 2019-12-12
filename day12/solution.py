
class Moon:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.dx = 0
        self.dy = 0
        self.dz = 0
        
    def energy(self):
        first = abs(self.x) + abs(self.y) + abs(self.z)
        second = abs(self.dx) + abs(self.dy) + abs(self.dz)
        return first * second
    
    def __str__(self):
        return '<x= ' + str(self.x) + ', y= ' + str(self.y) + ', z= ' + str(self.z) + '>'
#         return str(self.x) + ',' + str(self.y) + ',' + str(self.z) + ',' + str(self.dx) + ',' + str(self.dy) + ',' + str(self.dz)
        
    def applyGravity(self, o):
        if o.x > self.x:
            self.dx += 1
        elif o.x < self.x:
            self.dx -= 1
        if o.y > self.y:
            self.dy += 1
        elif o.y < self.y:
            self.dy -= 1
        if o.z > self.z:
            self.dz += 1
        elif o.z < self.z:
            self.dz -= 1
    
    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.z += self.dz

# inputString = open("input.txt", "r").read()
# moons = [Moon(17, -12, 13), Moon(2, 1, 1), Moon(-1, -17, 7), Moon(12, -14, 18)]

# inputString = open("test1.txt", "r").read()

# moons = [Moon(-1, 0, 2), Moon(2, -10, -7), Moon(4, -8, 8), Moon(3, 5, -1)]
#energy after 10 is 179, 2772 before repeat

# inputString = open("test2.txt", "r").read()
moons = [Moon(-8, -10, 0), Moon(5, 5, 10), Moon(2, -7, 3), Moon(9, -8, -3)]
# 4686774924

a = moons[0]
b = moons[1]
c = moons[2]
d = moons[3]
previous = set()
# 7030162386 too low
# 4686774924
for i in range(0, 4686774925):
#     current = (a.x, b.x, c.x, d.x, a.dx, b.dx, c.dx, d.dx) #18 #2028   1014  338
#     current = (a.y, b.y, c.y, d.y, a.dy, b.dy, c.dy, d.dy) #28 #5898 2949  983
#     current = (a.z, b.z, c.z, d.z, a.dz, b.dz, c.dz, d.dz) #44 #4702 2351 2351
    
    #56344
    #231614
    #193052
    #314917503970904
    current = (a.x, b.x, c.x, d.x, a.dx, b.dx, c.dx, d.dx, a.y, b.y, c.y, d.y, a.dy, b.dy, c.dy, d.dy, a.z, b.z, c.z, d.z, a.dz, b.dz, c.dz, d.dz)
    
    if current in previous:
        print(i)
        break
    else:
        previous.add(current)
        
#     if a.x < b.x:
#         a.dx += 1
#         b.dx -= 1
#     elif a.x > b.x:
#         a.dx -= 1
#         b.dx += 1
#     if a.x < c.x:
#         a.dx += 1
#         c.dx -= 1
#     elif a.x > c.x:
#         a.dx -= 1
#         c.dx += 1
#     if a.x < d.x:
#         a.dx += 1
#         d.dx -= 1
#     elif a.x > d.x:
#         a.dx -= 1
#         d.dx += 1
#     if b.x < c.x:
#         b.dx += 1
#         c.dx -= 1
#     elif b.x > c.x:
#         b.dx -= 1
#         c.dx += 1
#     if b.x < d.x:
#         b.dx += 1
#         d.dx -= 1
#     elif b.x > d.x:
#         b.dx -= 1
#         d.dx += 1
#     if c.x < d.x:
#         c.dx += 1
#         d.dx -= 1
#     elif c.x > d.x:
#         c.dx -= 1
#         d.dx += 1
         
    
#     if a.y < b.y:
#         a.dy += 1
#         b.dy -= 1
#     elif a.y > b.y:
#         a.dy -= 1
#         b.dy += 1
#     if a.y < c.y:
#         a.dy += 1
#         c.dy -= 1
#     elif a.y > c.y:
#         a.dy -= 1
#         c.dy += 1
#     if a.y < d.y:
#         a.dy += 1
#         d.dy -= 1
#     elif a.y > d.y:
#         a.dy -= 1
#         d.dy += 1
#     if b.y < c.y:
#         b.dy += 1
#         c.dy -= 1
#     elif b.y > c.y:
#         b.dy -= 1
#         c.dy += 1
#     if b.y < d.y:
#         b.dy += 1
#         d.dy -= 1
#     elif b.y > d.y:
#         b.dy -= 1
#         d.dy += 1
#     if c.y < d.y:
#         c.dy += 1
#         d.dy -= 1
#     elif c.y > d.y:
#         c.dy -= 1
#         d.dy += 1
          
#     if a.z < b.z:
#         a.dz += 1
#         b.dz -= 1
#     elif a.z > b.z:
#         a.dz -= 1
#         b.dz += 1
#     if a.z < c.z:
#         a.dz += 1
#         c.dz -= 1
#     elif a.z > c.z:
#         a.dz -= 1
#         c.dz += 1
#     if a.z < d.z:
#         a.dz += 1
#         d.dz -= 1
#     elif a.z > d.z:
#         a.dz -= 1
#         d.dz += 1
#     if b.z < c.z:
#         b.dz += 1
#         c.dz -= 1
#     elif b.z > c.z:
#         b.dz -= 1
#         c.dz += 1
#     if b.z < d.z:
#         b.dz += 1
#         d.dz -= 1
#     elif b.z > d.z:
#         b.dz -= 1
#         d.dz += 1
#     if c.z < d.z:
#         c.dz += 1
#         d.dz -= 1
#     elif c.z > d.z:
#         c.dz -= 1
#         d.dz += 1

    for moon in moons:
        for other in moons:
            if other != moon:
                moon.applyGravity(other)
    
    for moon in moons:
        moon.move()
        
print()
print('After Step: ' + str(i+1))
for moon in moons:
    print(str(moon))
    
total = 0
for moon in moons:
    total += moon.energy()
print(total)
#1351 too low
#2249 too low