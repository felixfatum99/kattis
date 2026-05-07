n = int(input())
current = input()
prev_x = current[0]
prev_y = current[1]
sum = 0
for _ in range(n-1):
    current = input()
    current_x = current[0]
    current_y = current[1]
    sum += abs(ord(prev_x)-ord(current_x))+abs(ord(prev_y)-ord(current_y))
    prev_x = current_x
    prev_y = current_y

print(sum)


