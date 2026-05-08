n = int(input())

left_side_up = {}
left_side_down = {}
right_side_up = {}
right_side_down = {}

for i in range(1, 9):
    left_side_down[-i] = "W"
    right_side_down[-i] = "W"
    right_side_up[+i] = "W"
    left_side_up[+i] = "W"

for i in range(n):
    d, c = map(str, input().split())
    if d[0] == "-" or d[0] == "+":
        #Right side
        tooth = int(d[1]) if d[0] == "+" else int(d[1]) * -1
        if c == "m":
            if tooth > 0:
                right_side_up.pop(tooth)
            else:
                right_side_down.pop(tooth)
        else:
            if tooth > 0:
                right_side_up[tooth] = "b"
            else:
                right_side_down[tooth] = "b"
    else:
        #Left side
        tooth = int(d[0]) if d[1] == "+" else int(d[0]) * -1
        if c == "m":
            if tooth > 0:
                left_side_up.pop(tooth)
            else:
                left_side_down.pop(tooth)
        else:
            if tooth > 0:
                left_side_up[tooth] = "b"
            else:
                left_side_down[tooth] = "b"

if "b" not in left_side_down.values() and "b" not in left_side_up.values() and len(left_side_up)>0 and len(left_side_down) > 0:
    print(1)
elif "b" not in right_side_down.values() and "b" not in right_side_up.values() and len(right_side_up)>0 and len(right_side_down) > 0:
    print(0)
else:
    print(2)