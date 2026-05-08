s = input()

output = 0
b = set()
has_used_one = False

for l in s:
    if l in b:
        continue
    else:
        a = s.count(l)
        if a == 1 and not has_used_one:
            has_used_one = True
        else:
            b.add(l)
            if a % 2 != 0:
                output += 1

print(output)
    