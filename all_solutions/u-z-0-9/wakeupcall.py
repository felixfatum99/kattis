a, b = map(int, input().split())

b1 = sum([int(x) for x in input().split(" ")])
b2 = sum([int(x) for x in input().split(" ")])

print("Button 1" if b1 > b2 else ("Button 2" if b2 > b1 else "Oh no"))

