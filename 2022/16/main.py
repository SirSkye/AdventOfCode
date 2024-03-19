def read():
    lines = dict()
    for _ in range(10): #66
        line = input().strip(",;").split()
        lines[line[1]] = [line[4][5:], line[9:]]
    return lines

def part1():
    pass