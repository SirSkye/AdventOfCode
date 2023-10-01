def read_data():
    with open(r"C:\Users\aisha\AdventOfCode\2022\5\part1\data.txt", 'r') as f:
        instructions = []
        stacks = []
        line = f.readline().strip("\n")
        for _ in range(0, len(line)//4 + 1):
            stacks.append([])
        while line != "":
            for i in range(0, len(line)//4 + 1):
                if (line[(4 * i) + 1] != ' ') and (line[(4 * i) + 1] > '9'):
                    stacks[i].append(line[(4 * i) + 1])
            line = f.readline().strip("\n")
        for line in f:
            instructions.append(line.strip("\n").split(" "))
    return stacks, instructions

def main():
    stacks, instructions = read_data()
    #print(stacks, instructions)
    for instruction in instructions:
        d_i = int(instruction[3]) - 1
        d_f = int(instruction[5]) - 1
        cargo = int(instruction[1])
        #breakpoint()
        stacks[d_f] = stacks[d_i][cargo-1::-1] + stacks[d_f]
        #breakpoint()
        stacks[d_i] = stacks[d_i][cargo:]
    print(list(stacks[x][0] for x in range(0, len(stacks))))

main()