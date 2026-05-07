d = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26,
    "_": 27,
    ".": 28,
}

def run():
    while True:
        inp = input().split(" ")
        if inp[0] == '0':
            break
        print(reverse_rot(int(inp[0]), inp[1]))

def reverse_rot(i, s):
    key_list = list(d.keys())
    val_list = list(d.values())
    output = ""
    for c in s:
        x = d.get(c)+i
        if x > 28:
            x = x -28
        position = val_list.index(x)
        output = key_list[position] + output
    return output

run()