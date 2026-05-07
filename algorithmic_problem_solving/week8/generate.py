import random 

N = 100
K = 1000

file_path = "/Users/felixfatum/Desktop/kattis/Algo_prob_solv/week8/super.txt"

with open(file_path, "w") as f:
    f.write(str(N)+" "+str(K)+"\n")
    for _ in range(K):
        c = random.randint(0, 1)
        if c == 0:
            f.write("F "+str(random.randint(1, N))+"\n")
        else:
            a = str(random.randint(1, N//2))
            b = str(random.randint(N//2+1, N))
            f.write("C "+a+" "+b+"\n")