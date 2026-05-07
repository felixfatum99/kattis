n = int(input())

line = [int(x) for x in input().split()]
sorted_line = sorted(line, reverse=True)

for q in sorted_line:
    for i in range(len(line)):
        if q == line[i]:
            print(i+1, end=" ")