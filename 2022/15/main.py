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

def part1():
    pairs = read()
    count = set()
    beacon_y = set()
    line_y = 2000000
    line_y = 10

    for pair in pairs:
        sensor = pair[0]
        beacon = pair[1]
        distance = abs((sensor.x - beacon.x)) + abs((sensor.y - beacon.y))
        r = distance - abs((line_y - sensor.y))
        print(f"{str((sensor.x, sensor.y)) : <8}{distance : ^5}{r : >2}")
        if r < 0:
            continue
        for x in range(sensor.x + r * -1, sensor.x + r+1):
            count.add(x)
        if beacon.y == line_y:
            beacon_y.add(beacon.y)
    return len(count - beacon_y)

def gen_point(center:Point, r:int, x:int):
    points = []
    if (center.y - (r - abs(center.x - x)) - 1) >= 0:
        points.append(Point(x, center.y - (r - abs(center.x - x)) - 1))
    if (center.y + (r - abs(center.x - x)) + 1) <= 4000000: #4000000
        points.append(Point(x, center.y + (r - abs(center.x - x)) + 1))
    return points

def part_2() -> Point:
    pairs = read()
    sphere_range = []

    for pair in pairs:
        sensor:Point = pair[0]
        beacon:Point = pair[1]
        
        r = abs(sensor.x - beacon.x) + abs(sensor.y - beacon.y)
        
        sphere_range.append([r, sensor])
        
    for pair in pairs:
        print(pair)
        in_bound = True
        sensor:Point = pair[0]
        beacon:Point = pair[1]
        # if sensor.x == 0:
        #     break
        
        r = abs(sensor.x - beacon.x) + abs(sensor.y - beacon.y)

        for x in range(max(0, r * -1+ sensor.x), min(r+1+sensor.x, 4000000)): #4000000
            for point in gen_point(sensor, r, x):
                for ranges in sphere_range:
                    bound  = ranges[0]
                    compare_sensor  = ranges[1]
                    dist = abs(point.x - compare_sensor.x) + abs(point.y - compare_sensor.y)
                    if dist <= bound:
                        in_bound = True
                        break #In bound, move to next point
                    in_bound = False
                if in_bound == False:
                    return point
        print(f"Finished {pair}")
    return None

point_int = part_2()
print(point_int)
print(point_int.x * 4000000 + point_int.y)




#4131712 -> Too low