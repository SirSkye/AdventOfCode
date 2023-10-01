def read_data():
    data = []
    with open(r"C:\Users\aisha\AdventOfCode\2022\8\part1\data.txt") as f:
        for line in f:
            #print(line,line.strip("\n"), [x for x in line.strip("\n")])
            data.append([x for x in line.strip("\n")])
    return data

def main():
    grid = read_data()
    #print(grid)
    count = 0
    for row, tree_list in enumerate(grid[1:-1]): #Techinically row refers to the one before
        print(tree_list)

        for col,tree in enumerate(tree_list[1:-1]):
            top = max([grid[x][col+1] for x in range(0, row+1)])
            bottom = max([grid[x][col+1] for x in range(row+2, len(grid[row+2:])+row+2)])
            right = max(tree_list[col+2:])
            left = max(tree_list[:col+1])
            print(f"Tree {tree}, {top, bottom, left, right}")
            if (tree > min(top, bottom, left, right)):
                count += 1
    count += (len(grid[0]) * 2) + ((len(grid) - 2) * 2)
    print(count)
main()

#6411, high