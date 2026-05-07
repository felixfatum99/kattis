import sys 

class fenwick:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n+1)

    def construct(self, arr):
        for i in range(self.size):
            self.update_bit(i, arr[i])
        
    def update_bit(self, index, value):
        index += 1

        while index <= self.size:
            self.tree[index] += value
            index += index & (-index)

    def get_sum(self, index):
        index += 1
        s = 0

        while index > 0:
            s += self.tree[index]
            index -= index & (-index)
        
        return s
    
    def sum_in_range(self, start, stop):
        return self.get_sum(stop) - self.get_sum(start-1)

inp = sys.stdin.buffer
N, Q = map(int, inp.readline().split())
fw = fenwick(N)

out = []
for _ in range(Q):
    parts = inp.readline().split()
    if parts[0] == b'+':
        i = int(parts[1])
        v = int(parts[2])
        fw.update_bit(i, v)
    else:
        k = int(parts[1])
        out.append(str(fw.get_sum(k - 1)))

sys.stdout.write("\n".join(out))