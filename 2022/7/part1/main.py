from collections import defaultdict
from pprint import pprint

def read_data():
    data = []
    with open(r"C:\Users\aisha\AdventOfCode\2022\7\part1\data.txt", 'r') as f:
        for line in f:
            data.append(line.strip("\n"))
    return data

def main():
    commands = read_data()
    sizes = defaultdict(int)
    where = []
    total = 0

    for command in commands:
        #print(command.split())
        match command.split():
            case ["$", "cd", "/"]:
                #breakpoint()
                where.clear()
                where.append("/")
            case ["$", "cd", ".."]:
                #breakpoint()
                where.pop()
            case ["$", "cd", directory]:
                #breakpoint()
                where.append(directory + "/")
            case ["$", ls]:
                pass
            case ["dir", directory]:
                pass
            case _:
                #breakpoint()
                for x in range(0, len(where)):
                    sizes["".join(where[0:x+1])] += int(command.split()[0])
    for k,v in sizes.items():
        if v <= 100000:
            total += v
    print(total)

    

main()