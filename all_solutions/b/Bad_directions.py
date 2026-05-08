#https://open.kattis.com/problems/baddirections
n = int(input())

for i in range(n):
    digit, n = input().split()
    digit = int(digit)
    numbers = [int(x) for x in n]

    for i in range(len(numbers)):
        numbers[i] = str((numbers[i]+digit) % 10)

    print("".join(numbers))