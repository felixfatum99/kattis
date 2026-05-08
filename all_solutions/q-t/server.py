a, b = map(int, input().split(" "))
c = 0

for i, n in enumerate(input().split(" ")):
    c+=int(n)
    if c > b:
        print(i)
        break
    elif i == a-1:
        print(a)
        