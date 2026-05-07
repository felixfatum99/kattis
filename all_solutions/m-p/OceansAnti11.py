n = int(input())
FibArray = [0, 1]

def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n < len(FibArray):
        return FibArray[n]
    else:        
        FibArray.append(fibonacci(n - 1) + fibonacci(n - 2))
        return FibArray[n]

for i in range(n):
    x = int(input())
    print(fibonacci(x+2) % (pow(10, 9)+7))

