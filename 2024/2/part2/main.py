def check_safe(levels):
    diffs = [levels[x+1] - levels[x] for x in range(len(levels)-1)]
    if all([x in range(-3, -1+1) for x in diffs]):
        return True
    elif all([x in range(1, 3+1) for x in diffs]):
        return True
    return False

if __name__ == "__main__":
    LINES = 1000
    safe_count = 0
    for x in range(LINES):
        numbers = [int(x) for x in input().split()]
        if check_safe(numbers):
            safe_count += 1
            continue
        else:
            for index in range(len(numbers)):
                temp_numbers = numbers.copy()
                temp_numbers.pop(index)
                if check_safe(temp_numbers):
                    safe_count += 1
                    break

    print(safe_count)