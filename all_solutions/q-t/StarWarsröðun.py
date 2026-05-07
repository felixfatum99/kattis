n = int(input())
numbers = sorted([int(x) for x in input().split()])
print(" ".join(str(x) for x in numbers[int(n/3):int((n/3)*2)]), " ".join(str(x) for x in numbers[:int(n/3)]), " ".join(str(x) for x in numbers[int((n/3)*2):]))

