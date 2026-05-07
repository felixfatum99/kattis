import math 

n = int(input())

for _ in range(n):
    number = int(input())
    output = ""

    if number % 2 != 0:
        output += "O"
    
    if int(math.sqrt(number))**2 == number:
        output += "S"

    print(output if output != "" else "EMPTY")