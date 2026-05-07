n, s = map(int, input().split(" "))
for i in range(n):
    l, h = map(int, input().split(" "))
    if s>=l and s<=h:
        s+=1
print(s)