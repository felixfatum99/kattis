r, c = map(int, input().split())
d = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
seats = []

for _ in range(c):
    rows = []
    for _ in range(r):
        rows.append(False)
    seats.append(rows)

s = int(input())
for _ in range(s):
    a, b = map(int, input().split())
    seats[a-1][b-1] = True



d_c = 0
for i in range(c):
    for j in range(r):
        if seats[i][j]:
            if i-1 >= 0:
                if seats[i-1][j]:
                    d_c += 1
                if j-1 >= 0:
                    if seats[i-1][j-1]:
                        d_c += 1
                if j+1 <= r-1:
                    if seats[i-1][j+1]:
                        d_c+=1
            if j-1 >= 0:
                if seats[i][j-1]:
                    d_c += 1
            if j+1 <= r-1:
                if seats[i][j+1]:
                    d_c += 1    
            if i+1 <= c-1:
                if seats[i+1][j]:
                    d_c += 1
                if j-1 >= 0:
                    if seats[i+1][j-1]:
                        d_c += 1
                if j+1 <= r-1:
                    if seats[i+1][j+1]:
                        d_c+=1
            d[d_c] += 1
            d_c = 0

for i in range(9):
    print(d[i], end=" ")