n = int(input())
print(" ".join(sorted([w[::-1] for w in input().split()], reverse=True)))