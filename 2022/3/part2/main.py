def read_data():
    data = []
    with open(r"C:\Users\aisha\AdventOfCode\2022\3\part1\data.txt", "r") as f:
        for line in f:
            data.append(line.strip("\n"))
    return data

def main():
    data = read_data()
    length = len(data)
    score = 0

    for x in range(0, length//3):
        letter = ''
        for i in data[x*3]:
            if((i in data[x*3+1]) and (i in data[x*3+2])):
                letter = i
                break
        if letter.islower():
            score += ord(letter)-96
            print("Score", ord(letter)-96)
        else:
            score += ord(letter)-38
            print("Score", ord(letter)-38)
    
    print(score)

main()