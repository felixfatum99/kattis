def run():
    n = int(input())
    m = int(input())
    
    a = int(0)

    for i in range(m):
        s = input()
        for j in range(n):
            if s[j] == ".":
                a += 1

    print(a / (n * m))
run()