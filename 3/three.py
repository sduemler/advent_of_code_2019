input = open("input_three.txt")
wireOneInput = input.readline()
wireTwoInput = input.readline()
wireOneInput = wireOneInput.split(",")
wireTwoInput = wireTwoInput.split(",")
wireOne = []
wireTwo = []

def calcWire(wire, wireInput):
    x = 0
    y = 0
    for a in wireInput:
        direction = a[0]
        length = int(a[1:])
        if(direction == "R"):
            for a in range(length):
                x = x + 1
                wire.append((x, y))
        if(direction == "L"):
            for a in range(length):
                x = x - 1
                wire.append((x, y))
        if(direction == "U"):
            for a in range(length):
                y = y + 1
                wire.append((x, y))
        if(direction == "D"):
            for a in range(length):
                y = y - 1
                wire.append((x, y))

calcWire(wireOne, wireOneInput)
calcWire(wireTwo, wireTwoInput)

crosses = []

for x in wireOne:
    if x in wireTwo:
        crosses.append(x)

distances = []
for x in crosses:
    distances.append(abs(x[0]) + abs(x[1]))

print(min(distances))
        
