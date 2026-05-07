import sys
data = sys.stdin.readlines()

for line in data:   
    print(line.replace("\n", ""), end="")
