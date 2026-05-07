A, B = map(int, input().split())
bowls = [int(x) for x in input().split()]

total = 0
for i in range(0, A-B+1, 1):
    total = max(total, sum(bowls[i:i+B]))

print(total)