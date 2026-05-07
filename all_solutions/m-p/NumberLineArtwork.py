class node:
    def __init__(self, val, next, prev):
        self.value = val
        self.next = next
        self.prev = prev


n, m = map(int, input().split())
original_color_line = input().split()
arms = []

for color in original_color_line:
    arms.append(node(color, None, None))

root = arms[0]

for i in range(n-1):
    arms[i].next = arms[i+1]
    arms[i+1].prev = arms[i]

for j in range(m):
    index, command = input().split()
    index = int(index)

    if command == "R":
        arms[index] = arms[index].next
    elif command == "L":
        arms[index] = arms[index].prev
    else:
        new = node(command, arms[index], arms[index].prev)
        arms[index].prev.next = new
        arms[index].prev = new
        arms[index] = new
    

while True:
    print(root.value)
    if root.next != None:
        root = root.next
    else:
        break

