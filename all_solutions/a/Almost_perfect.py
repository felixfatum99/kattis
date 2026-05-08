#https://open.kattis.com/problems/almostperfect
from math import isqrt
import sys

for line in sys.stdin:
    n = int(line)

    total = 1

    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            total += i

            if i != n // i:
                total += n // i

    if n == 1:
        total = 0

    if total == n:
        print(n, "perfect")
    elif abs(total - n) <= 2:
        print(n, "almost perfect")
    else:
        print(n, "not perfect")