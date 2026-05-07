n = int(input())
l = [int(x) for x in input().split(" ")]
l.sort()
print(l[len(l)-1], end=" ")
print(l[0])
