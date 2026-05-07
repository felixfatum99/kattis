g, r = map(int, input().split())

if g == 0:
    print(0)
else:
    if g < r:
        print(10*g)
    else:
        amount = r * 10
        g -= r
        if g > 0:
            while g >= 3:
                amount += 10
                g -= 3
            while g >= 2:
                amount += 3
                g -= 2
            while g > 0:
                amount += 1
                g -= 1
            print(amount)
        else:
            print(amount)