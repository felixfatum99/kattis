#https://open.kattis.com/problems/aldur
n = int(input())
youngest = float('inf')

for _ in range(n):
    youngest = min(youngest, int(input()))

print(youngest)