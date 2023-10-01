def read_data():
    data = [line.strip() for line in open(r"C:\Users\aisha\AdventOfCode\2022\11\part1\test.txt", "r").readlines()]
    stuff = {k : {} for k in range(0, ((len(data)+1)//7))}
    # for x, item in enumerate(data):
    #     print(x, item)
    for key in stuff.keys():
        stuff[key]["Items"] = [int(x) for x in (data[(key * 7)+ 1].replace(",", "").split(" ")[2:])]
        stuff[key]["Operation"] = data[(key * 7) + 2][17:]
        stuff[key]["Test"] = int(data[(key * 7) + 3][19:])
        stuff[key]["True"] = int(data[(key * 7) + 4][-1])
        stuff[key]["False"] = int(data[(key * 7) + 5][-1])
        stuff[key]["Count"] = 0
    return stuff

def main():
    monkeys = read_data()
    for x in range(0, 20):
        print(x)
        for y in range(0, max(monkeys.keys())+ 1):
            monkeys[y]["Count"] += len(monkeys[y]["Items"])
            for old in monkeys[y]["Items"]:
                new = (eval(monkeys[y]["Operation"]))
                if (new % monkeys[y]["Test"]) == 0:
                    monkeys[monkeys[y]["True"]]["Items"].append(new)
                else:
                    monkeys[monkeys[y]["False"]]["Items"].append(new)
                #breakpoint()
            monkeys[y]["Items"] = []
        #breakpoint()
        print(x, [monkeys[x]["Items"] for x in monkeys.keys()])
    print([monkeys[x]["Count"] for x in monkeys.keys()])

main()