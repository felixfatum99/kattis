n, q = map(int, input().split(" "))
output = ["?"]*n
villa = False
for i in range(q):
    x, y = map(str, input().split(" "))
    x = int(x)
    for j in range(len(y)):
        if output[x+j-1] == "?":
            output[x+j-1] = y[j]
        elif output[x+j-1] != y[j]:
            villa = True
            break

if villa:
    print("VILLA")
else:
    for c in output:
        print(c, end="")