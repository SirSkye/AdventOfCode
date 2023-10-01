def read_data() -> list:
    with open(r"2022\1\part1\data.txt", "r") as f:
            stuff = f.readlines()
    return stuff

def main():
    max = 0
    current = 0
    data = read_data()

    for item in data:
        if item == "\n":
            if current > max:
                max = current
            current = 0
            continue
        item.strip("\n")
        current += int(item)
    print(max)

main()