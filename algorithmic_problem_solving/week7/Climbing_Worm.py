a, b, h = map(int, input().split())
cp = 0
output = 0

while True:
    cp += a
    output += 1
    if cp >= h:
        break
    cp-=b

print(output)