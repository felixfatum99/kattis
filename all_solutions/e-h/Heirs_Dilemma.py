def run():
    x = input().split(" ")
    i = int(x[0])
    j = int(x[1])

    output = 0

    for p in range(i, j+1):
        z = str(p)
        if z.count("0") == 0:
            b = True
            for l in str(p):
                if z.count(l) > 1:
                    b = False
                    continue 
                if int(l) != 0:
                    if p % int(l) != 0:
                        b = False
                else:
                    b = False
            if b:
                output+= 1

    print(output)
run()