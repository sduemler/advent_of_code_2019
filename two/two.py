input = open("input_two.txt")
original = input.readlines()

def setup(original):
    opcodes = original
    opcodes = (str(opcodes[0]).split(","))
    opcodes = [int(i) for i in opcodes]
    return opcodes

def intcode(opcodes):
    for x in range(0, len(opcodes), 4):
        if(opcodes[x] == 1):
            opcodes[opcodes[x+3]] = opcodes[opcodes[x + 1]] + opcodes[opcodes[x + 2]]
        elif(opcodes[x] == 2):
            opcodes[opcodes[x+3]] = opcodes[opcodes[x + 1]] * opcodes[opcodes[x + 2]]
        elif(opcodes[x] == 99):
            break
        else:
            break
    return opcodes[0]

opcodes = setup(original)
opcodes[1] = 12
opcodes[2] = 2
print("Puzzle 1: " + str(intcode(opcodes))) # Puzzle 1 answer

for noun in range(100):
    for verb in range(100):
        opcodes = setup(original)
        opcodes[1] = noun
        opcodes[2] = verb
        # print(intcode(opcodes))
        if intcode(opcodes) == 19690720:
            print("Puzzle 2: " + str(100 * opcodes[1] + opcodes[2])) # Puzzle 2 answer

        


