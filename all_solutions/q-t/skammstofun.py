def run():
    n = int(input())
    m = input()
    x = m.split(" ")

    for i in x:
        if ord(i[0]) < 91 and ord(i[0]) > 64:
            print(i[0], end = "")

run()