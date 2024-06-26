import re

def write_debug(line):
    with open("e1.txt", "a") as f:
        f.write(line)
        f.write("\n")

def read():
    data = []
    for _ in range(1000):
        data.append(input())
    return data

def part_one():
    data = read()
    total = 0
    for line in data:
        number = 0
        for char in line:
            if (ord(char) >= ord("0")) and (ord(char) <= ord("9")):
                number += int(char) * 10
                break
        for char in line[::-1]:
            if (ord(char) >= ord("0")) and (ord(char) <= ord("9")):
                number += int(char)
                break
        total += number
    return total

def part_two():
    data = read()
    mapping = {
        "zero" : "0",
        "one" : "1",
        "two" : "2",
        "three" : "3",
        "four" : "4", 
        "five" : "5",
        "six" : "6",
        "seven" : "7",
        "eight" : "8",
        "nine" : "9"
    }
    total = 0
    for line in data:
            number = 0
            for char in line:
                if (ord(char) >= ord("0")) and (ord(char) <= ord("9")):
                    number += int(char) * 10
                    break
            for char in line[::-1]:
                if (ord(char) >= ord("0")) and (ord(char) <= ord("9")):
                    number += int(char)
                    break
            total += number
    return total

def part_two():
    data = read()
    total = 0

    mapping = {
        "zero" : 0,
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4, 
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9
    }

    for x in range(0, 10):
        mapping[str(x)] = x

    pattern = r"one|two|three|four|five|six|seven|eight|nine"
    first_patern = re.compile(rf"({pattern}|[0-9])")
    second_pattern = re.compile(rf"({pattern[::-1]}|[0-9])")

    for line in data:
        print(line)
        tens = first_patern.search(line).group()
        ones = second_pattern.search(line[::-1]).group()[::-1]
        print(tens, ones)
        total += mapping[tens]*10 + mapping[ones]
        write_debug(str(mapping[tens]*10 + mapping[ones]))

    return total

def matcher(char):
    mapping = {
        "zero" : 0,
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4, 
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9
    }
    return str(mapping[char.group(0)])

def part_twov2():
    data = read()
    for line in data:
        line = re.sub(rf"one|two|three|four|five|six|seven|eight|nine", matcher, line)
        print(line)



print(part_two())

#435 Too low