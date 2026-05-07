n = int(input())

d = {}
max_length = 0
for _ in range(n):
    line = input()
    max_length = max(max_length, len(line))
    for j in range(len(line)):
        if j in d.keys():
            a, b = d[j] 
            a+=ord(line[j])
            d[j] = (a, b+1)
        else:
            d[j] = (ord(line[j]), 1)

for i in range(max_length):
    print(chr(int(d[i][0]/d[i][1])), end="")