import sys
d = {}
for l in sys.stdin:
    command = l.split()

    if command[0] == "define":
        d[command[2]] = int(command[1])
    else:
        if command[1] in d and command[3] in d:
            if command[2] == "<":
                print(d[command[1]] < d[command[3]])
            elif command[2] == ">":
                print(d[command[1]] > d[command[3]])
            else:
                print(d[command[1]] == d[command[3]])
        else:
            print("undefined")
