import random

T = 5
M = 100000

numbers = [random.randint(0, pow(10, 9)) for _ in range(2*M)]
file_path = "/Users/felixfatum/Desktop/kattis/python_solutions/m-p/nesteddollsinput.txt"

with open(file_path, "w") as f:
    f.write(str(T)+"\n")
    for _ in range(T):
        f.write(str(M)+"\n")
        f.write(" ".join(map(str, numbers))+"\n")
        