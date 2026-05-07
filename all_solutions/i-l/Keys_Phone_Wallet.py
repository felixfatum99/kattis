def run():
    x = int(input())
    list = ["keys", "phone", "wallet"]
    for i in range(x):
        inp = input()
        if list.count(inp) > 0:
            list.remove(inp)
    if len(list) == 0:
        print("ready")
    else:
        for y in list:
            print(y)

run()