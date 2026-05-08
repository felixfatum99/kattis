#https://open.kattis.com/problems/busassignment
n = int(input())
inside = 0
max = 0
for i in range(n):
    a, b = map(int, input().split())
    inside-=a
    inside+=b
    if inside > max:
        max = inside
print(max)