import sys

direction = {
    "up": (0, -1),
    "down": (0, 1),
    "right": (1, 0),
    "left": (-1, 0)
}

x, y = 0, 0
c_x = [0]
c_y = [0]
d = {
    (0, 0): "S"
}

for line in sys.stdin:
    c = direction[line.replace("\n", "")]
    x += c[0]
    y += c[1]
    c_x.append(x)
    c_y.append(y)
    d[(x, y)] = "*"

d[(x, y)] = "E"

c_x_s = sorted(c_x)
c_y_s = sorted(c_y)

l_x, h_x = c_x_s[0], c_x_s[-1]
l_y, h_y = c_y_s[0], c_y_s[-1]

for j in range(l_y - 1, h_y + 2):
    row = []
    for i in range(l_x - 1, h_x + 2):
        if i == l_x - 1 or i == h_x + 1 or j == l_y - 1 or j == h_y + 1:
            row.append("#")
        else:
            if (i, j) in d:
                row.append(d[(i, j)])
            else:
                row.append(" ")
    print("".join(row))