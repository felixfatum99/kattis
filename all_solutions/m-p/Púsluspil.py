n, m = map(int, input().split())
puzzle_box = {}

for i in range(m):
    puzzle_box[i+1] = False

for i in range(n):
    info = [int(x) for x in input().split()]
    for j in range(1, info[0]+1):
        puzzle_box[info[j]] = True

if False in puzzle_box.values():
    print("Neibb")
else:
    print("Jebb")