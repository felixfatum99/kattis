N = int(input())
posts = [int(x) for x in input().split()]

total = 0
current = 0
for post in posts:
    total+=abs(post-current)
    current = post

print(total)