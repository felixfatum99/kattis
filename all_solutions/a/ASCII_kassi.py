#https://open.kattis.com/problems/asciikassi
n = int(input())

print("+", end = "")
for i in range(n):
    print("-", end = "")
print("+")

for j in range(n):
    print("|", end="")
    for k in range(n):
        print(" ", end="")
    print("|")

print("+", end = "")
for i in range(n):
    print("-", end = "")
print("+")