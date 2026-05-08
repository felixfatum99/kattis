#https://open.kattis.com/problems/apaxiaaans
name = input()
result = []
prev_char = None

for char in name:
    if char != prev_char:
        result.append(char)
        prev_char = char

print(''.join(result))