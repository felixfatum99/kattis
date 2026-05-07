n = int(input())

for i in range(1, n+1, 1):
    sum = 0
    cubed_sum = 0
    for j in range(1, i+1, 1):
        sum+=j
        cubed_sum += (j*j*j)
    print(sum*sum)
    print(cubed_sum)