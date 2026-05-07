n = int(input())
numbers = [(int(x), True) for x in input().split()]
numbers_two = numbers
for i in range(n):
    if i != 0 and numbers[i][0] < numbers[i-1][0]:
        numbers_two[i] = (numbers[i-1][0], False)

for t in numbers_two:
    if t[1]:
        print(t[0], end=" ")