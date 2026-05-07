x = input()
counter = 2
for c in x:
    if c == "b":
        if counter%2==0:
            print(0, end="")
        else:
            print(1, end="")
        counter+=1
    else:
        print(c, end="")