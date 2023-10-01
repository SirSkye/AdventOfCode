def read_data():
    data = []
    with open(r"C:\Users\aisha\AdventOfCode\2022\4\part1\data.txt", 'r') as f:
        for line in f:
            temp = line.strip("\n").split(",")
            temp[0] = [int(x) for x in temp[0].split("-")]
            temp[1] = [int(x) for x in temp[1].split("-")]
            data.append(temp)
        return data
#[['12', '88'], ['10', '11']] 12 10 yes???
def main():
    data = read_data()
    count = 0

    for pair in data:
        first = pair[0]
        second = pair[1]
        print(pair)
        if first[0] == second[0]:
            #print("yes")
            count += 1
        elif first[0] < second[0]:
            if first[1] >= second[1]:
                #print("yes")
                count += 1
        elif (second[0] < first[0]):
            print(second[0], first[0], second[0] < first[0])
            if second[1] >= first[1]:
                print("yes")
                count += 1
    print(count)


def old_main():
    data = read_data()
    count = 0
    for pair in data:
        print(pair)
        if pair[0][0] == pair[1][0]:
            if((pair[0][1] > pair[1][1]) or (pair[1][1] > pair[0][1])):
                count += 1
        elif pair[0][0] < pair[1][0]:
            if pair[0][1] >= pair[1][1]:
                count += 1
                print("1", pair)
        elif pair[1][0] < pair[0][0]:
            if pair[1][1] >= pair[0][1]:
                count += 1
                print("2", pair)
    print(count)
    #print(data)

main()

#514
#619
#779
#553