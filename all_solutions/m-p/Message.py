def run():
    i = input().split(" ")
    N = int(i[0])
    M = int(i[1])
    output = ""
    for j in range(N):
        n = input()
        for k in n:
            if k != ".":
                output = output + k

    print(output)
run()