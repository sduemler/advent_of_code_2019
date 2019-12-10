input = open("input_one.txt", "r")
lines = input.readlines()

baseFuel = 0
totalFuel = 0

for x in lines:
    baseFuel += ((int(x) // 3) - 2)
print(str(baseFuel) + " for all modules.")

for x in lines:
    mass = int(x)
    while(mass >= 0):
        mass = (mass // 3) - 2
        if(mass > 0):
            totalFuel += mass
print(str(totalFuel) + " for all modules and additional fuel.")