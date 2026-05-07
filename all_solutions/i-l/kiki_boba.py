def run():
    w = input()

    b = 0
    k = 0

    for l in w:
        if l == "k":
            k += 1
        if l == "b":
            b += 1

    if b > k:
        print("boba")
    elif k > b:
        print("kiki")
    elif b == 0 and k == 0:
        print("none")
    else:
        print("boki")

run()