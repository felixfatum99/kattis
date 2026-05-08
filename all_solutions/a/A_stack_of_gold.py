#https://open.kattis.com/problems/astackofgold
w, s = map(int, input().split())

tungsten = 29260
gold = 29370 

for i in range(1, s+1):
    res = 0
    for j in range(1, i):
        res += tungsten * j
    res += (gold * i) 
    for j in range(i+1, s+1):
        res += tungsten * j
    if res == w:
        print(i)