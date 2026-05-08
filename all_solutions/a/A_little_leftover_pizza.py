#https://open.kattis.com/problems/alittleleftoverpizza
a = int(input())

slices = {
    "S": 0,
    "M": 0,
    "L": 0
}

for i in range(a):
    size, amount = input().split()
    slices[size] += int(amount)

total_boxes = 0

for s in slices:
    amount = slices[s] 
    if s == "S" and amount != 0:
        if amount <= 6:
            total_boxes += 1
        else:
            total_boxes+= 1 + ((amount - (amount % 6))/6)
    elif s == "M" and amount != 0:
        if amount <= 8:
            total_boxes += 1
        else:
            total_boxes+= 1 + ((amount - (amount % 8))/8)
    elif s == "L" and amount != 0:
        if amount <= 12:
            total_boxes += 1
        else:
            total_boxes+= 1 + ((amount - (amount % 12))/12)

print(int(total_boxes))