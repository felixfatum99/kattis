l = input().split()
n = int(input())
unsorted = []
for i in range(n):
    info = tuple(input().split())
    unsorted.append(info)

s = int(input())

sort_keys = []
for j in range(s):
    sort_keys.append(l.index(input()))
    list = sorted(unsorted, key=lambda element : tuple(element[k] for k in reversed(sort_keys)))
    print(*l)
    for item in list:
        print(*item)
    print()


