def read_data():
    data = []
    with open(r"C:\Users\aisha\AdventOfCode\2022\2\part1\data.txt") as f:
        for line in f:
            data.append(line.strip("\n").split(" "))
    return data

def main():
    data = read_data()
    total = 0
    scoring_outcome = {
        'A': {
            'X' : 3,
            'Y' : 6,
            'Z' : 0
        },
        'B' : {
            'X' : 0,
            'Y' : 3,
            'Z' : 6
        },
        'C' : {
            'X' : 6, 
            'Y' : 0,
            'Z' : 3
        }
    }
    scoring_throw = {
        'X' : 1,
        'Y' : 2,
        'Z' : 3
    }
    for i in data:
        total += scoring_outcome[i[0]][i[1]] + scoring_throw[i[1]]
    
    print(total)
        



        
        

main()