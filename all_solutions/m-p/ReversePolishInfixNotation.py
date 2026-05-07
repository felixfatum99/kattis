from collections import deque

inp = input().split()

operators = {"*", "+", "-", "/"}
stack = deque()

for c in inp:
    if c not in operators:
        stack.append(c)
    else:
        right = stack.pop()
        left = stack.pop()
        res = "(" + left + c + right + ")"
        stack.append(res)

print(stack.pop())