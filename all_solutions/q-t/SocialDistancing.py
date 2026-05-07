n, m = map(int, input().split())
inp = [int(x) for x in input().split()]

correct = []
for i in range(n):
    correct.append(False)

for i in range(len(inp)):
    correct[inp[i]-1] = True

output = 0
for i in range(n):
    if i == 0:
        if not correct[0] and not correct[1] and not correct[n-1]:
            correct[0] = True
            output += 1
    elif not correct[i%n] and not correct[(i+1)%n] and not correct[(i+2)%n]:
        correct[(i+1)%n] = True
        output+=1


#print(correct)
print(output)