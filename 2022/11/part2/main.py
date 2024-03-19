import pprint as pp

def read() -> dict:
    data = {}
    for x in range(8):
        current = {}
        input()
        current["items"] = [int(x) for x in input().strip("Starting items: ").split(", ")]
        current["operation"] = input()[13:]
        current["Test"] = int(input().strip("Test: divisible by "))
        current["True"] = int(input()[-1])
        current["False"] = int(input()[-1])
        input()
        data[x] = current
    return data

def 

def main():
    monkeys = read()
    pp.pprint(monkeys)
    for monkey in range(8):
        

main()