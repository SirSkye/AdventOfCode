def read(num_lines:int):
    pairs = []
    for _ in range((num_lines-1)//3):
        pairs.append([eval(input()), eval(input())])
        input()
    return pairs

def part1(num_lines=451):
    packets = read(num_lines)
    for index, pair in enumerate(packets):
        left = pair[0]
        right = pair[1]
        

print(part1(25))