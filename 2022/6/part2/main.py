from collections import deque

def read_data():
    data = ''
    with open(r"C:\Users\aisha\AdventOfCode\2022\6\part1\data.txt", 'r') as f:
        data = f.readline()
    return data

def is_unique(x):
    return True if (len(set(x)) == 14) else False

def main():
    datastream = read_data()
    count = 0
    queue = deque([], 14)
    for x in range(0, 13):
        queue.append(datastream[x])
    datastream = datastream[13::]

    for x in range(0, len(datastream)):
        queue.append(datastream[x])
        print(queue, deque(set(queue)))
        if is_unique(queue):
            count = x + 14
            break
    print(count)     

main()