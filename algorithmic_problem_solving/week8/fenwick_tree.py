import sys

class fenwick:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size+1)
        self.output = []

    def lsb(self, index):
        return index & (-index)

    def add(self, index, value):
        while index <= self.size:
            self.tree[index] += value
            index += self.lsb(index)

    def sum(self, index):
        sum = 0
        while index > 0:
            sum += self.tree[index]
            index -= self.lsb(index)
        return sum 

    def command(self, line):
        if line[0] == b"+":
            self.add(int(line[1])+1, int(line[2]))
        else:
            self.output.append(str(self.sum(int(line[1]))))
    
    def print_res(self):
        sys.stdout.write("\n".join(self.output))

input = sys.stdin.buffer

N, Q = map(int, input.readline().split())
f_tree = fenwick(N)


for _ in range(Q):
    res = f_tree.command(input.readline().split())

f_tree.print_res()
