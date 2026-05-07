n, m = map(int, input().split(" "))
l = [0]*n
for i in range(n):
    x = int(input())
    l[x-1]+=1
l.sort(reverse=True)
if l[0]+m>=n:
    print("Ja")
else:
    print("Nej")