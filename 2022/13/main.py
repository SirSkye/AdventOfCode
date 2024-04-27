from ast import literal_eval
from itertools import zip_longest

def read(num_lines:int):
    pairs = []
    for _ in range((num_lines-1)//3):
        pairs.append([literal_eval(input()), literal_eval(input())])
        input()
    return pairs

def cmp(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return True

def part1(num_lines=451):
    packets = read(num_lines)
    for index, pair in enumerate(packets):
        left = pair[0]
        right = pair[1]

print(part1(25))

#int : int --> cmp
#List : List --> int:int