import sys 

input = sys.stdin.buffer.readline

a, b = map(int, input().split())
s = []

def rec(i, j, l, s):
    if i == j:
        return 1
    
    else:
        res = 0
        res += rec(i + 1, j, l, s)
        
        if all((elem, i) not in s for elem in l):
            l.append(i)
            res += rec(i+1, j, l, s)
            l.pop()
        return res

for i in range(b):
    x, y = map(int, input().split())
    s.append((min(x, y), max(x, y)))

print(rec(1, a+1, [], s))