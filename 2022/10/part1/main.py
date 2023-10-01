def read_data():
    with open(r"C:\Users\aisha\AdventOfCode\2022\10\part1\data.txt", "r") as f:
        data = [line.strip("\n") for line in f]
    return data

def main():
    instructions = read_data()
    cycle = 0
    register = 1
    cycle_val = []
    valid = [x*40 + 20 for x in range(0, 6)]
    for instruction in instructions:
        if instruction == "noop":
            cycle += 1
            if cycle in valid: cycle_val.append(register)
        else:
            print(instruction, register, cycle)
            cycle += 1
            if cycle in valid: cycle_val.append(register)
            cycle += 1
            if cycle in valid: cycle_val.append(register)
            register += int(instruction.split()[1])
            #if cycle > 180: print(instruction, register)
    print(cycle_val)
    print(sum([cycle_val[x]*(x*40+20) for x in range(0, 6)]))


main()

#16620 Too high