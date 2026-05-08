#https://open.kattis.com/problems/basicprogramming1
def run():
    inp = [int(x) for x in input().split(" ", -1)]
    inp_two = [int(x) for x in input().split(" ", -1)]
    
    if inp[1] == 1:
        print(7)

    if inp[1] == 2:
        if inp_two[0] > inp_two[1]:
            print("Bigger")
        elif inp_two[0] == inp_two[1]:
            print("Equal")
        else:
            print("Smaller")

    if inp[1] == 3:
        l = [inp_two[0], inp_two[1], inp_two[2]]
        print(l[1])
    
    if inp[1] == 4:
        print(sum(inp_two))
    
    if inp[1] == 5:
        print(sum(num for num in inp_two if not num%2))

    if inp[1] == 6:
        l = [num%26+97 for num in inp_two]
        ll = [chr(num) for num in l]
        for i in range(len(ll)):
            print(ll[i], end = "")

    if inp[1] == 7:
        i = 0 
        v = []
        while True:
            if inp_two[i] >= inp[0]:
                print("Out")
                break
            elif inp_two[i] == inp[0]-1:
                print("Done")
            else:
                i = inp_two[i]
                if i in v:
                    print("cyclic")
                    break
                v.append(i)

run()