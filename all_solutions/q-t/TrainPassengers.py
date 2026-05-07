C, n = map(int, input().split())

current_amount = 0
ouput = "Possible"

for i in range(n):
    line = input().split()
    if int(line[0]) > current_amount:
        ouput = "Impossible"
        break
    else:
        current_amount-=int(line[0])

    if int(line[1])+current_amount <= C:
        current_amount+=int(line[1])
    else:
       ouput = "Impossible"
       break
    if  int(line[2]) > 0 and current_amount != C:
        ouput = "Impossible"
        break
    if int(line[2]) > 0 and i == n-1:
        ouput = "Impossible"
        break

if current_amount != 0:
    ouput = "Impossible"

print(ouput)