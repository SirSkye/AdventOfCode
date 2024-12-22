if __name__ == "__main__":
    LINES = 1000
    safe_count = 0
    for x in range(LINES):
        numbers = [int(x) for x in input().split()]
        if numbers[1] - numbers[0] == 0:
            continue
        multiplier = (numbers[1] - numbers[0])/abs(numbers[1] - numbers[0])
        safe = True
        for i in range(len(numbers)-1):
            val = (numbers[i+1] - numbers[i])*multiplier
            if not ((val >= 1) and (val <=3)):
                safe = False
                break
        if safe:
            safe_count += 1
    print(safe_count)