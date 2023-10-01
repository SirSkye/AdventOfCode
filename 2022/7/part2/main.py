from collections import defaultdict
from pprint import pprint

def read_data():
    data = []
    with open(r"C:\Users\aisha\AdventOfCode\2022\7\part1\test.txt", 'r') as f:
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

    candidate = ["/", 70000000]
    
    for k,v in sizes.items():
        availiable = 70000000 - sizes["/"]
        need = 30000000 - availiable
        if (v >= need) and (v < candidate[1]):
            candidate.clear()
            candidate.append(k)
            candidate.append(v)
    print(candidate)

    

main()