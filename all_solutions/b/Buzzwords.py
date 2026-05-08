#https://open.kattis.com/problems/buzzwords
import sys

def find(x, m, base = 26, prime = 2**63 - 1):
    n = len(x)

    dict = {}

    multiplier = pow(base, m, prime)

    h = 0
    for ch in x[:m]:
        h = (h * base + ord(ch)) % prime

    for i in range(n - m + 1):
        if h not in dict:
            dict[h] = 0

        dict[h] += 1

        if i + m < n:
            old_char = ord(x[i])
            new_char = ord(x[i + m])

            h = (h * base) % prime
            h = h - (old_char * multiplier) % prime
            h = (h + new_char) % prime
    
    return dict

for line in sys.stdin:
    w = line.strip().replace(" ", "")
    for i in range(1, len(w)+1):
        res = sorted(list(find(w, i).values()), reverse=True)[0]
        if res < 2:
            break
        print(res)
    print()