from collections import defaultdict
class prefix:
    def __init__(self, arr):
        self.prefix = self.construct(arr)

    def construct(self, arr):
        temp = [0] * len(arr)
        for i, val in enumerate(arr):
            if i == 0:
                temp[i] = val
            else:
                temp[i] = temp[i-1]+val
        return temp

    def find_target_occurence(self, target=47):
        freq = defaultdict(int)
        freq[0] = 1
        count = 0

        for val in self.prefix:
            count += freq[val - target]
            freq[val] += 1

        return count
    
T = int(input())

for _ in range(T):
    input()
    N = int(input())
    arr = [int(x) for x in input().split()]
    prefix_arr = prefix(arr)
    print(prefix_arr.find_target_occurence())


