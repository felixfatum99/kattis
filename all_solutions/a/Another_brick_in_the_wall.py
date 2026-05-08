#https://open.kattis.com/problems/anotherbrick
h, w, n = map(int, input().split())
bricks = list(map(int, input().split()))

rows_done = 0
current_width = 0

for brick in bricks:
    current_width += brick

    if current_width == w:
        rows_done += 1
        current_width = 0

        if rows_done == h:
            break

    elif current_width > w:
        break

print("YES" if rows_done == h else "NO")