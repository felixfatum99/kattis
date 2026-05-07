def run():
    n = input()
    output = ""

    c = 1
    while True:
        output+=str(c)
        if(len(n)<=len(output)):
            break
        c+=1

    
    if output == n:
        print(c)
    else:
        print(-1)

run()
