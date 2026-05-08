#https://open.kattis.com/problems/bracketmatching
n = int(input())
line = input()
empty_stack = []
output = "Valid"

for i in range(len(line)):
    bracket = line[i]
    if bracket == "(" or bracket == "{" or bracket == "[":
        empty_stack.append(bracket)
    else:
        if len(empty_stack) < 1:
            output = "Invalid"
            break
        else:
            y = ord(bracket)
            x = ord(empty_stack.pop())
            if y-1 != x and y-2 != x:
                output = "Invalid"
                break
if len(empty_stack) > 0:
    output = "Invalid"
print(output)