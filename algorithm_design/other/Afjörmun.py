n = int(input())

for i in range(n):
    x = input().lower()
    print(x[0].upper(), end="")
    print(x[1:])