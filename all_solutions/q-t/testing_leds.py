st = float('inf')
for i in range(int(input())):
    s, O = map(int, input().split())
    if O == 0 and s < st:
        st = s
    
print(st if st != float('inf') else -1)