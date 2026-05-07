d = [4 for x in range(13)]

n = int(input())

for i in range(n):
    c = input()
    if c[0] == "J":
        c = "10"
    elif c[0] == "Q":
        c = "11"
    elif c[0] == "K":
        c = "12"
    elif c[0] == "A":
        c = "0"
    elif c[0] == "1" and c[1] == "0":
        c = "9"
    else:
        c = int(c[0])-1

    d[int(c)] -= 1


m = 0
for i in range(13):
    if d[i] > m:
        m = d[i]

print(m/(52-n))
