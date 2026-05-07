n = int(input())
output = True

for _ in range(n):
    height = int(input())
    output = (output & (height >= 48))

print(output)
