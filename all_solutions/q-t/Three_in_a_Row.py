def run():
    i = int(input())
    output = 0

    a = 1
    while True:
        x = a * (a+1) * (a+2)
        if x < i:
            output += 1
        else:
            break
        a += 1

    print(output)
run()