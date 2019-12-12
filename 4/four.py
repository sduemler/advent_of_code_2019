start = 347312
finish = 805915
countPasswords = 0

for x in range(start, finish):
    double = False
    doubles = 0
    strings = 0
    ascending = True
    check = str(x)
    countMatch = 0
    for y in range(len(check) - 1):
        if(int(check[y + 1]) < int(check[y])):
            ascending = False
        if(check[y + 1] == check[y]):
            if(countMatch == 0):
                doubles += 1
            elif(countMatch == 1):
                strings += 1
            countMatch += 1
        else:
            countMatch = 0
    if(doubles > strings):
        double = True
    if(double and ascending):
        countPasswords = countPasswords + 1
print(countPasswords)