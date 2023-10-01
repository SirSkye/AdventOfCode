def read_data():
    data = []
    with open(r"C:\Users\aisha\AdventOfCode\2022\3\part1\data.txt", "r") as f:
        for line in f:
            data.append(line.strip("\n"))
    return data

def main():
    data = read_data()
    score = 0
    for line in data:
        first, second = line[:len(line)//2], line[len(line)//2:]
        letter = ''
        for i in first:
            print(i)
            if i in second:
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