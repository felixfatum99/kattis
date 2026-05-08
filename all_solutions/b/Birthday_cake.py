#https://open.kattis.com/problems/birthdaycake
import math 

def dist(p1, p2):
    x = p2.real-p1.real
    y = p2.imag-p1.imag
    return math.sqrt(pow(x, 2)+pow(y, 2))

def inside_circle(p, r):
    return dist(p, complex(0, 0)) < r

def solve(candles, lines, pieces, n):
    if pieces > n:
        return "no"
    pos = set()
    for c in candles:
        temp = []
        for l in lines:
            equation = (l[0].real*c.real + l[0].imag*c.imag + l[1]).real > 0
            temp.append(equation)
        pos.add(tuple(temp))

    return "yes" if len(pos) == n else "no"

def pieces(lines, r, m):
    pieces = 1+m

    for i, line_1 in enumerate(lines):
        for j, line_2 in enumerate(lines):
            if i >= j:
                continue 

            a1 = line_1[0].real
            b1 = line_1[0].imag 
            c1 = line_1[1]

            a2 = line_2[0].real
            b2 = line_2[0].imag 
            c2 = line_2[1]

            d = a1*b2 - a2*b1

            if d == 0:
                continue

            x = (b1*c2 - b2*c1) / (a1*b2-a2*b1)
            y = (c1*a2 - c2*a1) / (a1*b2 - a2*b1)

            intersection = complex(x, y)
            if inside_circle(intersection, r):
                pieces += 1

    return pieces

n, m , r = map(int, input().split())
candles = []
lines = []

for _ in range(n):
    candle = complex(*map(float, input().split()))
    candles.append(candle)

for _ in range(m):
    a, b, c = map(int, input().split())
    line = (complex(a, b), c)
    lines.append(line)

total_pieces = pieces(lines, r, m)
#print(total_pieces)
print(solve(candles, lines, total_pieces, n))