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

    moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)] #(x, y)
    count = 0
    
    for y, line in enumerate(word_map):
        for x, letter in enumerate(line):
            cord = (x, y)
            if letter == "A":
                m_count = 0
                s_count = 0
                for move in moves:
                    add_cord = add(cord, move)
                    if not check_valid(add_cord, len(line), len(word_map)):
                        break
                    if word_map[add_cord[1]][add_cord[0]] == "M":
                        m_count += 1
                    elif word_map[add_cord[1]][add_cord[0]] == "S":
                        s_count += 1
                if (m_count == 2) and (s_count == 2):
                    corner_a = add(cord, moves[0])
                    corner_b = add(cord, moves[3])
                    if word_map[corner_a[1]][corner_a[0]] != word_map[corner_b[1]][corner_b[0]]:
                        count += 1
    print(count)