from collections import namedtuple

POINT = namedtuple("Point", ["x", "y"])

def read(num:int):
    data = []
    for _ in range(num):
        points =[]
        line = input().replace("-", "").replace(">", "").split()
        for point in line:
            points.append(POINT._make(point.split(",")))
        data.append(points)
    return data

def part_one(num:int = 147):
    data = read()
    sand_count = 0

    while True:
        '

print(read(2))