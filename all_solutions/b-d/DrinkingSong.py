def run(): 
    N = int(input())
    drink = input()

    while N > 0 : 
        if(N==1):
            print(N, "bottle of", drink, "on the wall,", N, "bottle of", drink+".")
            print("Take it down, pass it around, no more bottles of", drink+".")
        elif(N==2): 
            print(N, "bottles of", drink, "on the wall,", N, "bottles of", drink+".")
            print("Take one down, pass it around,", N-1, "bottle of", drink, "on the wall.")
            print()
        else: 
            print(N, "bottles of", drink, "on the wall,", N, "bottles of", drink+".") 
            print("Take one down, pass it around,", N-1, "bottles of", drink, "on the wall.")
            print()
        N = N-1
run()