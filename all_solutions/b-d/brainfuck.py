import sys

arr = [0] * 800000
index = 400000
command_index = 0

commands = sys.stdin.read().replace(" ", "").replace("\n", "")

bracket_map = {}
stack = []
for i, c in enumerate(commands):
    if c == "[":
        stack.append(i)
    elif c == "]":
        j = stack.pop()
        bracket_map[i] = j
        bracket_map[j] = i

output = []
while command_index < len(commands):
    x = commands[command_index]
    if x == "<":
        index-=1
    elif x == ">":
        index += 1
    elif x == "+":
        arr[index] = (arr[index] + 1) % 256
    elif x == "-":
        arr[index] = (arr[index] - 1 ) % 256
    elif x == ".":
        output.append(chr(arr[index]))
    elif x == "[":
        if arr[index] == 0:
            command_index = bracket_map[command_index]
    elif x == "]":
        if arr[index] != 0:
            command_index = bracket_map[command_index]

    command_index+=1

print("".join(output))