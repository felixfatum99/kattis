n,p,q = map(int, input().split(" "))
s = p+q
if s < n:
    print("paul")
else:
    s -= s % n
    t = s/n
    if t % 2 == 0:
        print("paul")
    else:
        print("opponent")
