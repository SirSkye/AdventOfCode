if __name__ == "__main__":
    LINES = 6
    total = 0

    for x in range(LINES):
        line = input()
        length = len(line)
        i = 0
        enabled = True

        while True:
            first = 0
            second = 0
            is_valid = True

            if (i >= length):
                break
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
            if is_valid and enabled:
                total += first * second
            i += 1
            print(i)
        print(total)