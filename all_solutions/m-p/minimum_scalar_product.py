import sys
input = sys.stdin.buffer.readline

t = int(input())

for i in range(t):
    n = int(input())
    l1 = [int(x) for x in input().split(" ", -1)]
    l1.sort(reverse=True)
    l2 = [int(x) for x in input().split(" ", -1)]
    l2.sort(reverse=False)
    sum = 0
    for z in range(n):
        sum += l1[z]*l2[z]
    print("Case #"+str(i+1)+":",sum)