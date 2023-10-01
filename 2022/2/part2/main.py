def read_data():
    data = []
    with open(r"C:\Users\aisha\AdventOfCode\2022\2\part2\data.txt") as f:
        for line in f:
            data.append(line.strip("\n").split(" "))
    return data

def main():
    data = read_data()
    total = 0
    scoring_outcome = {
        'A': { #Rock
            'X' : 3, #Lose
            'Y' : 1, #Draw
            'Z' : 2  #Win
        },
        'B' : { #Paper
            'X' : 1,
            'Y' : 2,
            'Z' : 3
        },
        'C' : { #Scissors
            'X' : 2, 
            'Y' : 3,
            'Z' : 1
        }
    }
    scoring_throw = {
        'X' : 0,
        'Y' : 3,
        'Z' : 6
    }
    for i in data:
        total += scoring_outcome[i[0]][i[1]] + scoring_throw[i[1]]
    
    print(total)
        
main()