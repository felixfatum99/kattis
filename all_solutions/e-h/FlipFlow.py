t, s, n = map(int, input().split())
up = True
top = 0
bottom = s
prev_time = 0


a_i_list = [int(x) for x in input().split()]
for i in range(n):
    a_i = a_i_list[i]
    if prev_time == 0:
        prev_time = a_i
        up = False
    else:
        sand = a_i-prev_time
        prev_time = a_i
        if up:
            flow = min(top, sand)
            top -= flow
            bottom += flow
        else:
            flow = min(bottom, sand)
            bottom -= flow
            top += flow
        up = not up

if up:
    print(top-(t-prev_time))
else:
    res = bottom-(t-prev_time)
    print(res if res > 0 else 0)