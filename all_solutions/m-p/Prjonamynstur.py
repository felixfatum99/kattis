def run():
    dict = {".": 20, "O": 10, "\\": 25, "/": 25, "A": 35, "^": 5, "v": 22}
    x = input().split(" ")
    n = int(x[0])
    m = int(x[1])

    output = int(0)

    for i in range(n):
        s = input()
        if "O" in s or "\\" in s or "/" in s or "A" in s or "^" in s or "v" in s:
            for j in range(m):
                output += dict[s[j]]
        else:
            output += m*20

    print(output)
run()

