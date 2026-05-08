import math
def run():
    n = int(input())
    m = input().split(" ")
    output = int(0)

    for i in range(n):
        output += int(m[i])

    print(math.floor(output / n))
run()