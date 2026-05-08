#https://open.kattis.com/problems/askmarilyn
import random 
choices = ['A', 'B', 'C']

for i in range(1000):
    random_pick = choices[random.randint(0, 2)]
    print(random_pick)

    l, n = map(str, input().split())
    print(l if n == '1' else " ".join(choices).replace(random_pick, "")[random.randint(0, 1)] if n == random_pick else " ".join(choices).replace(random_pick, "").replace(l, "").strip())

    input()