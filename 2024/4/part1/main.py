def add(a:tuple, b:tuple) -> tuple:
    return (a[0] + b[0], a[1] + b[1])

def check_valid(a:tuple, length_x:int, length_y: int) -> bool:
    x = a[0]
    y = a[1]
    if (x>=0) and (x <= (length_x - 1)):
        if (y >= 0) and (y <= (length_y - 1)):
            return True
    return False

if __name__ == "__main__":
    LINES = 140
    word_map = list()
    for x in range(LINES):
        word_map.append(input())

    word = "XMAS"
    moves = [(0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0)] #(x, y)
    count = 0
    
    for y, line in enumerate(word_map):
        for x, letter in enumerate(line):
            cord = (x, y)
            if letter == word[0]:
                for move in moves:
                    valid = True
                    next_cord = cord
                    for i in range(3):
                        next_cord = add(next_cord, move)
                        if not check_valid(next_cord, len(line), len(word_map)):
                            valid = False
                            break
                        if word_map[next_cord[1]][next_cord[0]] != word[i + 1]:
                            valid = False
                            break
                    if valid:
                        count += 1
    print(count)
                    