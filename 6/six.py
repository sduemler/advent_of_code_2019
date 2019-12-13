input = open("input.txt")

orbitDict = {}

orbit = input.readline()
while(orbit):
    orbitSplit = orbit.split(")")
    orbitSplit[-1] = orbitSplit[-1].strip()
    if(orbitSplit[1] not in orbitDict.keys()):
        orbitDict[orbitSplit[1]] = [orbitSplit[0]]
    else:
        orbitDict[orbitSplit[1]].append(orbitSplit[0])
    orbit = input.readline()

def findOrbits(orbitDict):
    direct = 0
    indirect = 0
    for x in orbitDict:
        direct += 1
        y = x
        while(orbitDict[y][0] in orbitDict.keys()):
            indirect += 1
            y = orbitDict[y][0]
    print("Direct: " + str(direct))
    print("Indirect: " + str(indirect))
    print("Total: " + str(direct + indirect))

def minOrbitalTransfers(orbitDict):
    numTransfers = 0
    yourTransfers = 0
    santaDistance = 0
    yourPath = []
    santaPath = []
    possibleTranfers = []
    x = 'YOU'
    y = 'SAN'
    while(orbitDict[x][0] in orbitDict.keys()):
        yourPath.append(orbitDict[x][0])
        x = orbitDict[x][0]
    while(orbitDict[y][0] in orbitDict.keys()):
        santaPath.append(orbitDict[y][0])
        y = orbitDict[y][0]
    for a in yourPath:
        yourTransfers += 1
        santaDistance = 0
        for b in santaPath:
            santaDistance += 1
            if a == b:
                possibleTranfers.append(yourTransfers + santaDistance - 2)
    print("Min transfers: " + str(min(possibleTranfers)))

findOrbits(orbitDict)
minOrbitalTransfers(orbitDict)


