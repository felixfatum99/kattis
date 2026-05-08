#https://open.kattis.com/problems/arithmeticadaptation
n = int(input())
if n > 1:
    print(1,n-1)
elif n == 1:
    print(-1, 2)
elif n == 0:
    print(-1,1)
elif n < -1:
    print(n+1,-1)
elif n == -1:
    print(-2, 1)