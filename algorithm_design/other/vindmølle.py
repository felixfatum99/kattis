a = int(input())
b = int(input())

if a > b:
    r = (360-a)+b
    l = a-b
    if r<=l:
        print(r)
    else:
        print(-l)
else:
    r = b-a
    l = (360-b)+a
    if r<=l:
        print(r)
    else:
        print(-l)

