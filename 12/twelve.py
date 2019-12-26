input = open("input.txt")
io = input.readline()
europa = input.readline()
ganymede = input.readline()
callisto = input.readline()

def setupPlanet(planet):
    planet = planet.split(",")
    planet[0] = planet[0][3:]
    planet[1] = planet[1][3:]
    planet[2] = planet[2][3:-2]
    planet = list(map(int, planet))
    planet = [planet, [0,0,0]]
    return planet

planets = [io, europa, ganymede, callisto]
planets = list(map(setupPlanet, planets))

pastPlanets = planets

for x in range(1000):
    for y in range(len(planets)):
        for z in range(len(planets)):
            if planets[y][0][0] > planets[z][0][0]:
                planets[y][1][0] -= 1
            if planets[y][0][0] < planets[z][0][0]:
                planets[y][1][0] += 1
            if planets[y][0][1] > planets[z][0][1]:
                planets[y][1][1] -= 1
            if planets[y][0][1] < planets[z][0][1]:
                planets[y][1][1] += 1
            if planets[y][0][2] > planets[z][0][2]:
                planets[y][1][2] -= 1
            if planets[y][0][2] < planets[z][0][2]:
                planets[y][1][2] += 1
    for y in range(len(planets)):
        planets[y][0][0] += planets[y][1][0]
        planets[y][0][1] += planets[y][1][1]
        planets[y][0][2] += planets[y][1][2]



totalEnergy = 0
for x in range(len(planets)):
    potentialEnergy = abs(planets[x][0][0]) + abs(planets[x][0][1]) + abs(planets[x][0][2])
    kineticEnergy = abs(planets[x][1][0]) + abs(planets[x][1][1]) + abs(planets[x][1][2])
    totalEnergy += potentialEnergy * kineticEnergy

print("Total Energy: " + str(totalEnergy))