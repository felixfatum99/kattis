#https://open.kattis.com/problems/alphabetspam

s = input()

w = sum(c == '_' for c in s)
l = sum(c.islower() for c in s)
u = sum(c.isupper() for c in s)
c = len(s) - w - l - u

print(w / len(s))
print(l / len(s))
print(u / len(s))
print(c / len(s))