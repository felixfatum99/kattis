n, r, c = map(int, input().split(" "))
rc = [[""]*c]*r
for i in range(r):
    names = [x for x in input().split(" ")]
    rc[i] = names
for i in range(n):
    name = input()
    if i%c == 0:
        if name == rc[int(i/c)][0]:
            print("left")
        else:
            print("right")
    elif i > n-c-1:
        break
        