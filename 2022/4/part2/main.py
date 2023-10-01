def read_data():
    data = []
    with open(r"C:\Users\aisha\AdventOfCode\2022\4\part1\data.txt", 'r') as f:
        for line in f:
            temp = line.strip("\n").split(",")
            temp[0] = [int(x) for x in temp[0].split("-")]
            temp[1] = [int(x) for x in temp[1].split("-")]
            data.append(temp)
        return data
    
def main():
    data = read_data()
    count = 0

    for pair in data:
        first = pair[0]
        second = pair[1]
        print(pair)
        
        if (first[0] != second[1]) and (second[0] != first[1]):
            if ((first[0] < second[0]) and (first[1] < second[1])) and (first[1] < second[0]):
                print("1yes")
                count += 1
            elif (second[0] < first[0]) and (second[1] < first[1]) and (second[1] < first[0]):
                print("2yes")
                count += 1
    print(1000 - count)


main()

#482 : Low
#648 : Low