import sys

def can_be_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

lines = sys.stdin.read().splitlines()

for j in range(len(lines)):
    line = lines[j].split()
    name = ""
    time = 0
    div = 0

    for i in range(len(line)):
        if can_be_float(line[i]):
            time+=float(line[i])
            div+=1
        else:
            name+=line[i]+" "

    print(time/div, name)