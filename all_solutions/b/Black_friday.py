#https://open.kattis.com/problems/blackfriday
n = int(input())
line = input()
players = line.split(" ")

def find(n, res):
    for j in range(n):
        if players[j] == res:
            print(j+1)

one = line.count("1")
two = line.count("2")
three = line.count("3")
four = line.count("4")
five = line.count("5")
six = line.count("6")

if six == 1:
    find(n, "6")
elif five == 1:
    find(n, "5")
elif four == 1:
    find(n, "4")
elif three == 1:
    find(n, "3")
elif two == 1:
    find(n, "2")
elif one == 1:
    find(n, "1")
else:
    print("none")

def find(n, res):
    for j in range(n):
        if players[j] == res:
            print(j+1)