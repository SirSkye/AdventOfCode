def read_data():
    with open(r"C:\Users\aisha\AdventOfCode\2022\10\part1\data.txt", "r") as f:
        data = [line.strip("\n") for line in f]
    return data
def main():
    instructions = read_data()
    cycle = 0
    register = 1
    sprite_draw = [[], [], [], [], [], []]
    for instruction in instructions:
        if instruction == "noop":
            index = (cycle)//40
            if index < 6:
                if (cycle%40) in [x for x in range(register-1, register+2)]:
                    sprite_draw[index].append('#')
                else:
                    print(cycle, cycle%40)
                    sprite_draw[index].append(".")
            cycle += 1
            #breakpoint()
        else:
            #print(instruction, register, cycle)
            index = (cycle)//40
            if index < 6:
                if (cycle%40) in [x for x in range(register-1, register+2)]:
                    sprite_draw[index].append('#')
                else:
                    sprite_draw[index].append(".")
            cycle += 1
            #breakpoint()
            index = (cycle)//40
            if index < 6:
                if (cycle%40) in [x for x in range(register-1, register+2)]:
                    sprite_draw[index].append('#')
                else:
                    sprite_draw[index].append(".")
            cycle += 1
            #breakpoint()
            register += int(instruction.split()[1])
            #if cycle > 180: print(instruction, register)
    for x in range(0, 6):
        #print(len(sprite_draw[x]))
        print("".join(sprite_draw[x]))


main()

#16620 Too high
#ELZUZHLR
#E