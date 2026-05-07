import bisect

def compute_p(l):
    n = len(l)
    finish_times = [interval[1] for interval in l]
    p = [0] * (n + 1)
    
    for j in range(1, n + 1):
        start_time = l[j-1][0]
        index = bisect.bisect_right(finish_times, start_time)
        p[j] = index
    
    return p

n = int(input())
m = [None]*(n+1)
intervals = []

for i in range(n):
    s, f, w = map(int, input().split(" "))
    intervals.append((s, f, w))

intervals.sort(key=lambda p: p[1])

p=compute_p(intervals)
m[0] = 0

for j in range(1, n+1, 1):
    m[j] = max((intervals[j-1][2]+m[p[j]]), m[j-1])

print(m[n])