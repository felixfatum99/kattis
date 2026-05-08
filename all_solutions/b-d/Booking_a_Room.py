n, r = map(int, input().split())

booked_rooms = set(int(input()) for _ in range(r))

for room in range(1, n + 1):
    if room not in booked_rooms:
        print(room)
        break
else:
    print("too late")
