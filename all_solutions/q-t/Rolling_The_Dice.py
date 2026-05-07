instr = input()
new_instr = ""

for l in instr:
    if l == 'd' or l == '+':
        new_instr += " "
    else:
        new_instr += l

a, b, c = map(int, new_instr.split())
res = (a+(a*b)+(2*c))/2

print(int(res) if res % 2 == 0 else res)