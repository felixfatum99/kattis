#https://open.kattis.com/problems/standings
import sys
input = sys.stdin.buffer.readline

t = int(input())

for _ in range(t):
    input()
    n = int(input())
    l = []

    for _ in range(n):
        name, number = input().split()
        l.append(int(number))
    
    print(sum(abs(nr-(i+1)) for i, nr in enumerate(sorted(l))))