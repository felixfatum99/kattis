#https://open.kattis.com/problems/abc
nums = sorted(map(int, input().split()))
print(*(nums[ord(c) - ord('A')] for c in input()))