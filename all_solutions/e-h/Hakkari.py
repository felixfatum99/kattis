def h():
    p = [int(z) for z in input().split(" ", -1)]
    output = []
    for i in range(p[0]):
        s = input()
        for x in range(len(s)):
            if s[x] == "*":
                output.append((i+1, x+1))

    print(len(output))
    for i in range(len(output)):
        print(output[i][0], output[i][1])
h()