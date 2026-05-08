#https://open.kattis.com/problems/rationalsequence2
def fraction_to_index(p, q):
    bits = []

    while p != 1 or q != 1:
        if p > q:
            k = (p - 1) // q
            bits.extend("1" * k)
            p -= k * q
        else:
            k = (q - 1) // p
            bits.extend("0" * k)
            q -= k * p

    n = 1
    for b in reversed(bits):
        n = n * 2 + int(b)

    return n


t = int(input())

for _ in range(t):
    case, frac = input().split()
    p, q = map(int, frac.split("/"))

    print(case, fraction_to_index(p, q))