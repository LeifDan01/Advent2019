

file = open("input.txt", "r").read()
# file = open("test.txt", "r").read()

entries = file.split("\n")

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
    print(things)
    planets[things[1]] = planet(things[1], things[0])

for planet in planets.values():
    if planet.orbits == 'COM':
        planet.orbits = False
    else:
        planet.orbits = planets[planet.orbits]

count = 0
for planet in planets.values():
    if planet:
        count += planet.countOrbits()

print(count)