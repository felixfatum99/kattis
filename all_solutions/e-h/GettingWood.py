s = input()

found = False
for i in range(len(s)):
    if s[i] == 't':
        if s[i:i+4] == 'tree':
            print(i)
            found = True
            break
if not found:
    print("no trees here")