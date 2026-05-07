temp = -30 #+8 degrees needed
oxygen = 0 #14% oxygen lvl needed 
oceans = 0 #9 % coverage needed

n = int(input())

for i in range(n):
    change, value = input().split()
    if change == "temperature":
        temp += int(value[1])
    if change == "oxygen":
        oxygen += int(value[1])
    if change == "ocean":
        oceans += int(value[1])

if temp >= 8 and oxygen >= 14 and oceans >= 9:
    print("liveable")
else:
    print("not liveable")
