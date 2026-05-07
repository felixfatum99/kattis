t = int(input())

for i in range(t):
    n = int(input())

    c = 3
    answer = 0
    while True: 
        if n >= (c*c)-1:
            answer += 1
            c = c+2
        else:
            print(answer)
            break