#https://open.kattis.com/problems/addingwords
import sys

d = {}
d_i = {}

for line in sys.stdin:
    command = line.replace("\n", "")

    if command == "clear":
        d.clear()
        d_i.clear()
        continue

    commands = command.split(" ")

    if commands[0] == "def":
        if commands[1] in d:
            del d_i[d[commands[1]]] 
        d[commands[1]] = int(commands[2])
        d_i[int(commands[2])] = commands[1]

    elif commands[0] == "calc":
        op = "+"
        res = 0
        for i in range(1, len(commands)-1, 1):
            if commands[i] == "+" or commands[i] == "-":
                op = commands[i]
            elif commands[i] not in d:
                res = float('inf')
                break
            else:
                if op == "+":
                    res += d[commands[i]]
                else:
                    res -= d[commands[i]]
        
        if res == float('inf') or res not in d_i:
            print(" ".join(commands[1:]), "unknown")
        else:
            print(" ".join(commands[1:]), d_i[res])