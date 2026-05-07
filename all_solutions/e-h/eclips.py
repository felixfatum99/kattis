s = input().split()
output = False
for w in s:
    if "e" in w:
        print(w, end=" ")
        output = True

if not output:
    print("oh noes")