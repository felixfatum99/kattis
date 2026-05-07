import bisect 

a = [(1, 2), (3, 4), (10, 9), (5, 1), (7, 7), (19, 1), (1, 19), (10, 89)]
a = sorted(a, key=lambda element: (element[0], -element[1]))
i = bisect.bisect_left(a, (3, -5))
print(a, i)