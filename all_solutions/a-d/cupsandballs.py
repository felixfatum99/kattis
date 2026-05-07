G = int(input())
N = int(input())
cups = ["no ball", "ball", "no ball"]

for i in range(N):
    a, b = map(int, input().split())
    temp = cups[a-1]
    cups[a-1] = cups[b-1]
    cups[b-1] = temp

if cups[G-1] == "ball":
    if G == 1:
        print(2, 3)
    elif G == 2:
        print(1, 3)
    else:
        print(1, 2)
else:
    if G == 1 and cups[1] == "ball":
       print(1, 2)
    if G == 1 and cups[2] == "ball":
       print(1, 3)
    if G == 2 and cups[0] == "ball":
       print(1, 2)
    if G == 2 and cups[2] == "ball":
       print(2, 3)
    if G == 3 and cups[0] == "ball":
       print(1, 3)
    if G == 3 and cups[1] == "ball":
       print(2, 3)