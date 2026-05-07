s = list(input())
s2 = list(input())

for i in range(len(s2)):
    l = s2.pop(0)
    if len(s)!= 0 and l == s[0]:
        s.pop(0)

print("Ja" if len(s) == 0 else "Nej")



