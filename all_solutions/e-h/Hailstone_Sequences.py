def run():
    inp = int(input())
    print(h_s(inp, 1))

def h_s(n, aux):
    if n == 1:
        return aux
    elif n % 2 == 0:
        return h_s((n/2), aux+1)
    else:
        return h_s((3*n)+1, aux+1)

run()