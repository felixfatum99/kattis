r, c = map(int, input().split())

island = []
for _ in range(r):
    island.append(input())

output = 0
A, B = 0, 0
for i in range(1, r-1):
    for j in range(1, c-1):
        if island[i-1][j-1] == "O" and island[i-1][j] == "O" and island[i-1][j+1] == "O" and island[i][j-1] == "O" and island[i][j+1] == "O" and island[i+1][j-1] == "O" and island[i+1][j] == "O" and island[i+1][j+1] == "O" and island[i][j] == "0":
            output+=1
            A, B = i, j

if output == 1:
    print(A+1, B+1)
else:
    text = "Oh no!" if output == 0 else "Oh no! "+str(output)+" locations"
    print(text)