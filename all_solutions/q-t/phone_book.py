n = int(input())

sum = 0
for _ in range(n):
    number = input()
    if number[:3] == "+39" and (len(number) == 13 or len(number) == 12):
        sum+=1
print(sum)