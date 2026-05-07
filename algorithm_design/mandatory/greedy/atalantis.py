def atlantis():
    x = int(input())

    s = []

    for i in range(x):
        t, a = map(int, input().split(" "))
        c = t+a 
        s.append([t, a, c])
    
    s.sort(key=lambda x: (x[2], x[0], x[1]))

    cwl = 0
    sum = 0
    for l in s:
        if cwl+l[0]<=l[1]:
            sum+=1
            cwl += l[0]
    print(sum)
atlantis()

