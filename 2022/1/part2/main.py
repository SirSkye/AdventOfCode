def read_data() -> list:
    with open(r"2022\1\part1\data.txt", "r") as f:
            stuff = f.readlines()
    return stuff

def main():
    top_calories = [1, 2, 3]
    data = read_data()
    current = 0

    for i in data:
            if i == "\n":
                if current > top_calories[0]:
                        if current > top_calories[1]:
                            if current > top_calories[2]:
                                    top_calories = top_calories[1:]
                                    top_calories.append(current)
                            else:
                                top_calories[0] = top_calories[1]
                                top_calories[1] = current
                        else:
                              top_calories[0] = current
                current = 0
                continue 
            current += int(i)
    print(top_calories[0] + top_calories[1] + top_calories[2])

main()