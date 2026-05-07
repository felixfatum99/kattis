import math
import random

n, m = 10000, 500000

intervals = [0 for _ in range(math.ceil(m/100)+1)]

for _ in range(n):
    b, d = random.randint(1000, 7200), random.randint(100, 1800)
    start_time = b
    while(start_time < m):
        for i in range(math.ceil(start_time/100), math.ceil(start_time/100)+math.ceil(d/100)):
            if i >= len(intervals):
                break
            intervals[i]+=1
        start_time+=d+b

print(max(intervals))