#Uses multiprocessing to speed up calculation time for part2 of the solution

import multiprocessing
import re
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

def read()-> list[list[Point]]:
    pairs = []
    for _ in range(29): #29
        line = input()
        nums = [int(x) for x in re.findall(r"([-]?\d+)", line)]
        pairs.append([Point._make((nums[0], nums[1])), Point._make((nums[2], nums[3]))])
    return pairs

def gen_point(center:Point, r:int, x:int) -> list[Point]:
    points = []
    if (center.y - (r - abs(center.x - x)) - 1) >= 0:
        points.append(Point(x, center.y - (r - abs(center.x - x)) - 1))
    if (center.y + (r - abs(center.x - x)) + 1) <= 4000000: #4000000
        points.append(Point(x, center.y + (r - abs(center.x - x)) + 1))
    return points

def calc_points(pair:list[Point]):
    pass

def part_2() -> Point:
    pairs = read()
    sphere_range = list()

    for pair in pairs:
        sensor:Point = pair[0]
        beacon:Point = pair[1]
        
        r = abs(sensor.x - beacon.x) + abs(sensor.y - beacon.y)
        
        sphere_range.append([r, sensor])

print(read())