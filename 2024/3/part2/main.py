if __name__ == "__main__":
    LINES = 6
    total = 0
    enabled = True
    line = " "
    for x in range(LINES):
        line += input().strip(r"\n")
    length = len(line)
    i = 0

    while True:
        first = 0
        second = 0
        is_valid = True

        if (i >= length):
            break
        if (line[i] == "d") and (line[i + 1] == "o") and (line[i + 2] == "(") and (line[i + 3] == ")"):
            i += 1
            enabled = True
            continue
        if (line[i] == "d") and (line[i + 1] == "o") and (line[i + 2] == "n") and (line[i + 3] == "'") and (line[i+4] == "t") and (line[i + 5] == "(") and (line[i+6] == ")"):
            enabled = False
            i+=1
            continue
        if (line[i] == "m") and (line[i+1] == "u") and (line[i+2] == "l") and (line[i+3] == "("):
            j = i+4
            while line[j].isdigit():
                first = first*10+int(line[j])
                j += 1
            if line[j] == ",":
                j += 1
                while line[j].isdigit():
                    second = second *10 + int(line[j])
                    j += 1
                if line[j] != ")":
                    is_valid = False
            else:
                is_valid = False
        else:
            is_valid = False
        if is_valid and enabled:
            total += first * second
        i += 1
    print(total)