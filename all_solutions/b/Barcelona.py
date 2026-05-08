#https://open.kattis.com/problems/barcelona

a = input().split()
b = input().split()

for i in range(int(a[0])):
    if b[i] == a[1]:
        if i == 0:
            print("fyrst")
        elif i == 1:
            print("naestfyrst")
        else:
            print(i+1, "fyrst")