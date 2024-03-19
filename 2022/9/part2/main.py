import math

def read_data():
    data = []
    with open(r"C:\Users\aisha\AdventOfCode\2022\9\part1\data.txt", "r") as f:
        for line in f:
            data.append(line.split())
    return data

def rounding(num):
    return ((num > 0) - (num < 0)) * int(abs(num) + 0.5)


def move_tail(H:tuple, T: tuple) -> tuple:
    distance = math.dist(H, T)
    #print(round((H[0] - T[0])/2))
    if distance <= 1.5:
         return T
    else:
        T = (T[0] + (rounding(((H[0] - T[0])/2)))), (T[1] + rounding(float((H[1] - T[1])/2)))

    #     T = (T[0] + ((H[0] - T[0])//2)), (T[1] + ((H[1] - T[1])//2))
    # else:
    #     if H[0] < T[0]:
    #         T = (H[0] - 1, T[1])
    #     else:
    #         T = (H[1] + 1, T[1])
    #     if H[1] < T[0]:
    #         T = (T[0], H[1] + 1)
    #     else:
    #         T = (T[0], H[1] - 1)
    return T

movements = read_data()
positions = [(0, 0) for x in range(10)]
visited = set()

for movement, steps in movements:
    x = 0
    y = 0
    match movement:
        case "D":
            y = -1
        case "U":
            y = 1
        case "L":
            x = -1
        case "R":
            x = 1
    print(movement, steps)
    for _ in range(0, int(steps)):
        positions[0] = (positions[0][0] + x, positions[0][1] + y)
        for i in range(1, 10):
            print(x)
            positions[i] = move_tail(positions[i-1], positions[i])
        print(positions)
        visited.add(positions[9])
    
print(visited)
print(len(visited))