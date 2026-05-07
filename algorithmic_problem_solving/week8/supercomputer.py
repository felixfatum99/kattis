class fenwick:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size+1)
        self.bytes = [0] * (size+1)

    def lsb(self, index):
        return index & (-index)

    def add(self, value, index):
        while index <= self.size:
            self.tree[index] += value
            index += self.lsb(index)
    
    def flip(self, index):
        value = -1 if self.bytes[index] == 1 else 1
        self.add(value, index)
        self.bytes[index] += value

    def sum(self, index):
        sum = 0
        while index > 0:
            sum += self.tree[index]
            index -= self.lsb(index)
        return sum 
    
    def range_query(self, start, stop):
        return self.sum(stop) - self.sum(start-1)
    
    def command(self, line):
        if line[0] == "F":
            self.flip(int(line[1]))
        else:
            print(self.range_query(int(line[1]), int(line[2])))


N, K = map(int, input().split())
f_tree = fenwick(N)

for _ in range(K):
    f_tree.command(input().split())