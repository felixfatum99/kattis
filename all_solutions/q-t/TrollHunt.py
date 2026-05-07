import math


def run():
    list= input()
    res = [int(x) for x in list.split(" ")]
    output = 0
    while res[0] > 1:
        output = output+1
        res[0] -= math.floor(res[1]/res[2])

    print(output)
run()