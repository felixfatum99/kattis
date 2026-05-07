import math
a, b = map(int, input().split())
bill = "1"+("0"*b)
bill = int(bill)
rest = (a % bill)
bottom = (a-rest)
top = bottom + bill
bottom_d = a-bottom
top_d = top-a

if bottom_d == top_d:
    print(top)
elif bottom_d < top_d:
    print(bottom)
else:
    print(top)