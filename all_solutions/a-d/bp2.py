N, t = map(int, input().split())
numbers = [int(x) for x in input().split()]

def one():
    output = "No"
    for i in range(N):
        for j in range(i, N):
            if numbers[i] + numbers[j] == 7777:
                output = "Yes"
                break
    print(output)

def two():
    output = "Unique"
    for i in range(N):
        if numbers.count(numbers[i]) > 1:
            output = "Contains duplicate"
            break
    print(output)

def three():
    output = -1
    for i in range(N):
        if numbers.count(numbers[i]) > N/2:
            output = numbers[i]
            break
    print(output)

def four():
    numbers.sort()
    if N % 2 == 0:
        print(numbers[int((N/2)-1)], numbers[int(N/2)])
    else:
        print(numbers[int((N-1)/2)])
        
def five():
    numbers.sort()
    for i in range(N):
        if numbers[i] > 999:
            break
        if numbers[i] >= 100 and numbers[i] <= 999:
            print(numbers[i], end=" ")
    return 

if t == 1:
    one()
elif t == 2:
    two()
elif t == 3:
    three()
elif t == 4:
    four()
elif t == 5:
    five()
