def read_data():
    data = []
    with open(r"C:\Users\aisha\AdventOfCode\2022\8\part1\data.txt") as f:
        for line in f:
            #print(line,line.strip("\n"), [x for x in line.strip("\n")])
            data.append([x for x in line.strip("\n")])
    return data

def search_tree(tree, view):
    #print(view, end='')
    for x in range(0, len(view)):
        if view[x] >= tree:
            return x+1
    return len(view)

def main():
    grid = read_data()
    #print(grid)
    max = 0
    for row, tree_list in enumerate(grid[1:-1]): #Techinically row refers to the one before
        #print(tree_list)
        for col,tree in enumerate(tree_list[1:-1]):
            top = search_tree(tree, [grid[x][col+1] for x in range(0, row+1)][::-1])
            bottom = search_tree(tree, [grid[x][col+1] for x in range(row+2, len(grid[row+2:])+row+2)])
            right = search_tree(tree, tree_list[col+2:])
            left = search_tree(tree, tree_list[:col+1][::-1])
            #print(f"Tree {tree}, {top, bottom, left, right}")
            if max < (top*bottom*right*left):
                max = (top*bottom*right*left)
    print(max)
main()

#6411, high