def run():
    inp = input()
    output = 0
    for c in inp:
        ascii = ord(c)
        if (ascii > 64 and ascii < 91) or (ascii > 96 and ascii < 123):
            output += 1
    print(output)
run()
