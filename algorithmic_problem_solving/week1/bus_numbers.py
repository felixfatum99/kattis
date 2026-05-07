n = int(input())
busses = sorted([int(x) for x in input().split(" ")])

prev_bus = -1
count = 0

for i, bus in enumerate(busses):
    if bus != prev_bus+1:
        if count >= 2:
            print("-" + str(prev_bus), end="")
            count = 0
        elif count > 0:
            print(" " + str(prev_bus), end="")
            count = 0
        print(" " + str(bus) if i != 0 else bus, end="")
        prev_bus = bus
    else:
        prev_bus = bus
        count += 1
        if i == len(busses)-1 and count >= 2:
            print("-" + str(prev_bus), end="")
        elif i == len(busses)-1:
            print(" " + str(bus) if i != 0 else bus, end="")