points = int(input())

ppk = int(input())
ppa = int(input())

outcomes = []

for i in range(int((points - (points % ppk))/ppk)+1):
    for j in range(int((points - (points % ppa))/ppa)+1):
        if (ppk*i) + (ppa*j) == points:
            outcomes.append((i, j))

if len(outcomes) != 0:
    print(len(outcomes))
    for pair in outcomes:
        print(pair[0], pair[1])
else:
    print(1)
    print(0, 0)



