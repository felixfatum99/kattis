#https://open.kattis.com/problems/biladlyklabord
s = input()
l = s[0]
print(l, end="")
for i in range(1, len(s), 1):
    if s[i] != l:
        print(s[i], end="")
    l = s[i]