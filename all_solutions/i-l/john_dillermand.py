h, w = map(int, input().split())

picture = []

for i in range(h):
    row = list(input())
    picture.append(row)

r, c = 0, 0
character = ""
while True:
    character = picture[r][c]
    picture[r][c] = "."

    
    if c != 0 and picture[r][c-1] != "." and picture[r][c-1] != character:
        c-=1
    
    elif c != w-1 and picture[r][c+1] != "." and picture[r][c+1] != character:
        c+=1
    
    elif r != 0 and picture[r-1][c] != "." and picture[r-1][c] != character:
        r-=1
    
    elif r != h-1 and picture[r+1][c] != "." and picture[r+1][c] != character:
        r+=1
    
    else:
        break

for row in picture:
    print("".join(row))