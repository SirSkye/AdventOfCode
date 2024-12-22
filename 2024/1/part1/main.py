def read(num:int) -> tuple[list]:
    left = list()
    right = list()
    for x in range(num):
        line = input().split()
        print(line)
        left.append(int(line[0]))
        right.append(int(line[1]))
    return left, right

if __name__ == "__main__":
    LINES = 1000
    left, right = read(LINES)
    dist = 0
   
    for x in range(1000):
       l_max = max(left)
       left.remove(l_max)
       r_max = max(right)
       right.remove(r_max)
       dist += (abs(l_max - r_max))
    print(dist)