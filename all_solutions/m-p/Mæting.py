def run():
    d = dict()
    s = int(input())

    for i in range(s):
        name = input()
        d.update({name: 0})
        #print(d.get(name))
    
    c = int(input())

    for x in range(c):
        inp = input().split(" ")
        for t in range(int(inp[0])):
            d.update({inp[t+1]: d.get(inp[t+1])+1})

    a = sorted(d.keys(), key=d.get)

    for x in reversed(a):
        print(d.get(x), x)

    
run()