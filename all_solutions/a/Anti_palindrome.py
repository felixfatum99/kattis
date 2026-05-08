#https://open.kattis.com/problems/antipalindrome
import re

text = input()
line = ''.join(re.findall(r'[a-zA-Z]', text)).lower()

p = "Anti-palindrome"

for i in range(len(line)):
    for j in range(i + 2, len(line) + 1):
        substring = line[i:j]
        if substring == substring[::-1]:
            p = "Palindrome"
            break
    if p == "Palindrome":
        break

print(p)