def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

a, b, k = map(int, input().split())

output = 0
for i in range(a, b+1, 1):
    temp = True
    for j in range(2, k+1):
        line = "".join(map(str, numberToBase(i, j)))
        if line != line[::-1]:
            temp = False
            break
    output += 1 if temp else 0

print(output)