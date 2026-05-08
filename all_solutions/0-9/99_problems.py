#https://open.kattis.com/problems/99problems
n = int(input())
target = 99
diff = abs(n-target)

while True:
    target += 100

    if abs(n-target) > diff:
        print(target-100)
        break

    diff = abs(n-target)