
file = open("input.txt", "r").read()
# file = open("test.txt", "r").read()
file = open("mitch.txt", "r").read()

entries = file.split("\n")
origin = None

class planet:
    def __init__(self, name, orbits):
        self.name = name
        self.orbits = orbits

    def countOrbits(self):
        orbits = self.orbits
        count = 1
        while orbits:
            count += 1
            orbits = orbits.orbits
        return count

planets = {}
for entry in entries:
    things = entry.split(')')
    planets[things[1]] = planet(things[1], things[0])

for planet in planets.values():
    if planet.orbits == 'COM':
        origin = planet
        planet.orbits = False
    else:
        planet.orbits = planets[planet.orbits]

#find earliest shared
def findShare():
    current = planets['YOU'].orbits
    while current.orbits:
        dest = planets['SAN'].orbits
        while dest:
            if current.orbits == dest:
                return dest
            dest = dest.orbits
        current = current.orbits

def distance(current, dest):
    count = 0
    while current != dest:
        count += 1
        current = current.orbits
    return count

shared = findShare()
# print(shared.name)
# print(distance(planets['YOU'].orbits, shared))
# print(distance(planets['SAN'].orbits, shared))
print(distance(planets['YOU'].orbits, shared) + distance(planets['SAN'].orbits, shared))

for planet in planets:
    count = 0
    for orbiting in planets.values():
        if orbiting.orbits and orbiting.orbits.name == planet:
            count += 1
    if count > 1:
        print(str(count) + ' orbit: ' + planet)
    

