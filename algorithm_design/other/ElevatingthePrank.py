A, B = map(int, input().split(" "))
m = min(A, B)
ma = max(A, B)
sum = (ma-m)*4
for i in range(int(input())):
    f = int(input())
    if f > m and f < ma:
        sum+=10
print(sum)