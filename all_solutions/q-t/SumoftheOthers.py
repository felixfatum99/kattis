import sys

data = sys.stdin.read().splitlines()
for l in data:
    line = [int(x) for x in l.split()]
    for i in range(len(line)):
        a = sum(line[:i]+line[i+1:])
        b = line[i]
        if a == b:
            print(b)
            break