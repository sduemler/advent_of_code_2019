input = open("input_one.txt", "r")
lines = input.readlines()
totalFuel = 0
for x in lines:
    totalFuel += ((int(x) // 3) - 2)
print(totalFuel)