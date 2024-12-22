from collections import defaultdict

if __name__ == "__main__":
    LINES = 1000
    left = list()
    right = defaultdict(int)

    for x in range(LINES):
        numbers = input().split()
        left.append(int(numbers[0]))
        right[int(numbers[1])] += 1

    score = 0

    for key in left:
        score += key * right[key]

    print(left, right)
    print(score)