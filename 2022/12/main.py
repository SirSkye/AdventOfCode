from queue import Queue

def read():
    height_map = []
    start_pos = None
    end_pos = None

    for y in range(41):
        current = []
        for x, char in enumerate(input()):
            if char == "S":
                start_pos = (x, y)
                char = "a"
            elif char == "E":
                end_pos = (x, y)
                char = "z"
            current.append(char)
        height_map.append(current)
    return height_map, start_pos, end_pos, len(height_map)-1, len(height_map[0])-1

def neighbour(heightmap, pos, max_x, max_y):
    found = []
    #Right
    if pos[0] < max_x:
        if ord(heightmap[pos[1]][pos[0]])+1 >= ord(heightmap[pos[1]][pos[0] + 1]):
            found.append((pos[0]+1, pos[1]))
    #Left
    if pos[0] > 0:
        if ord(heightmap[pos[1]][pos[0]])+1 >= ord(heightmap[pos[1]][pos[0] - 1]):
            found.append((pos[0]-1, pos[1]))
    #Up
    if pos[1] > 0:
        if ord(heightmap[pos[1]][pos[0]])+1 >= ord(heightmap[pos[1] - 1][pos[0]]):
            found.append((pos[0], pos[1]-1))
    #Down
    if pos[1] < max_y:
        if ord(heightmap[pos[1]][pos[0]])+1 >= ord(heightmap[pos[1] + 1][pos[0]]):
            found.append((pos[0], pos[1]+1))

    return found

def part1():
    heightmap, start, end, max_y, max_x = read()
    frontier = Queue()
    came_from = dict()

    frontier.put(start)
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()

        if current == end:
            break
        for next in neighbour(heightmap, current, max_x, max_y):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current
    
    current = end
    path = list()
    while current != start:
        path.append(current)
        current = came_from[current]
    return(len(path))

def calculate(heightmap, start, end, max_y, max_x):
    frontier = Queue()
    came_from = dict()

    frontier.put(start)
    came_from[start] = None

    found = False

    while not frontier.empty():
        current = frontier.get()

        if current == end:
            found = True
            break
        for next in neighbour(heightmap, current, max_x, max_y):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current
    
    if found == True:
        current = end
        path = list()
        while current != start:
            path.append(current)
            current = came_from[current]
        return(len(path))
    return None

def part2():
    heightmap, _, end, max_y, max_x = read()
    minimum = 999999999
    possible = []
    
    for y, line in enumerate(heightmap):
        for x, char in enumerate(line):
            if char == "a":
                possible.append((x, y))
    
    for a in possible:
        distance = calculate(heightmap, a, end, max_y, max_x)
        if distance != None:
            if distance < minimum:
                minimum = distance
    
    return minimum

print(part2())
# heightmap, start, end, max_y, max_x = read()
# print(max_x, max_y)
# print(heightmap[1][4])
# print(neighbour(heightmap, (4, 1), max_x, max_y))