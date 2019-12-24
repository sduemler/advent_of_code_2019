input = open("input.txt")
pixels = input.readline()

width = 25
height = 6
iterations = len(pixels) // (width * height)
layers = []
layerNum = 0
leastZeroes = 0
zeroesLayer = 0

for x in range(iterations):
    zeroes = 0
    layer = []
    for a in range(height):
        row = []
        for b in range(width):
            pixel = pixels[((layerNum * width * height) + (a*width)) + b]
            if pixel == '0':
                zeroes += 1
            row.append(pixel)
        layer.append(row)
    if leastZeroes == 0:
        leastZeroes = zeroes
    if zeroes < leastZeroes:
        leastZeroes = zeroes
        zeroesLayer = layerNum
    layers.append(layer)
    layerNum += 1

ones = 0
twos = 0
for x in layers[zeroesLayer]:
    for y in x:
        if y == '1':
            ones += 1
        if y == '2':
            twos += 1

# print(ones * twos)

image = []
for x in range(height):
    row = []
    for y in range(width):
        row.append(0)
    image.append(row)

for x in range(len(layers)):
    for y in range(len(layers[x])):
        for z in range(len(layers[x][y])):
            if image[y][z] == 0 and layers[x][y][z] != '2':
                if layers[x][y][z] == '0':
                    image[y][z] = '-'
                if layers[x][y][z] == '1':
                    image[y][z] = 'X'

for x in image:
    line = ''
    for y in x:
        line += str(y) + ' '
    print(line)
