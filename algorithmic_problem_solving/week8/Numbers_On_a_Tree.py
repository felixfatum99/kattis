info = input().split()
h = int(info[0])
root = pow(2, h+1)-1
l, r = 1, 2
current_val = root
lvl = 1

if len(info) == 1:
    print(root)
else:
    for val in info[1]:
        if val == 'R':
            current_val -= r
            r *= 2
            l = r-1
        else:
            current_val -= l
            l *= 2
            r = l+1
    print(current_val)