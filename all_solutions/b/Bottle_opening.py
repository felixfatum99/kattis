#https://open.kattis.com/problems/bottleopening
bottles = int(input())
needed = int(input())

if needed > bottles-1:
    print("impossible")
else:
    for i in range(needed):
        print("open", i+1, "using", i+2)