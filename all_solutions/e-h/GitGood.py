from collections import deque
N = int(input())

stack = deque()
s = set()

for i in range(N):
    command, f = input().split()

    if command == "cd":
        if f == ".." and stack:
            stack.pop()
        else:
            stack.append(f)
    elif command == "nano":
        path = ""
        for v in stack:
            path += v+"/"
        s.add(path+f)

s = sorted(list(s))

for val in s:
    print("git add", val)

print("git commit")
print("git push")