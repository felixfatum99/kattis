#https://open.kattis.com/problems/barshelf
import sys 
from bisect import bisect_left
input = sys.stdin.readline

class fenwick:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n+1)

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

N = int(input())
arr = [int(x) for x in input().split()]
sorted_vals = sorted(set(arr))
rank = {v: i for i, v in enumerate(sorted_vals)}
arr = [rank[x] for x in arr]

fenwick_tree_left = fenwick(N)
fenwick_tree_right = fenwick(N)

greater_to_the_left = [0]*(N+1)
smaller_to_the_right = [0]*(N+1)

for i in range(N):
    iterated_left = i
    pos = bisect_left(sorted_vals, 2*arr[i])
    sum = fenwick_tree_left.get_sum(pos-1)
    greater_to_the_left[i+1] = iterated_left-sum
    fenwick_tree_left.update_bit(arr[i], 1)

print()