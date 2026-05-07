def gift():
    i = int(input())
    score = -1
    name = ""

    for x in range(i):
        line = input().split(" ")
        if int(line[1]) > score:
            score = int(line[1])
            name = line[0]
    
    print(name)

gift()
