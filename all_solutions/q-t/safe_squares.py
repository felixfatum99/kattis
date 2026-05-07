board = [["." for _ in range(8)] for _ in range(8)]
for i in range(8):
    line = input()
    for j in range(8):
        if line[j] == "R":
            board[i][j] = "R"
            for k in range(i):
                board[k][j] = "R"
            for l in range(i, 8, 1):
                board[l][j] = "R"
            board[i] = ["R" for _ in range(8)]

sum = 0

for i in range(8):
    sum += "".join(board[i]).count(".")

print(sum)