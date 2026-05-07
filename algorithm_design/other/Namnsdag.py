def check_name(n, nn):
    sum = 0
    for i in range(len(n)):
        if n[i] != nn[i]:
            sum+= 1
    return sum
printed = False
name = input()
n = int(input())
for i in range(n):
    n_name = input()
    if not printed:
        if len(n_name) == len(name):
            if check_name(name, n_name) < 2:
                print(i+1)
                printed = True



