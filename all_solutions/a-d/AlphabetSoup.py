letters = input()
output = set()
for i in range(65, 65+26, 1):
    if chr(i) not in letters:
        output.add(chr(i))

print("".join(sorted(output)) if output else "Alphabet Soup!")
