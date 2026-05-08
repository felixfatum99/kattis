#https://open.kattis.com/problems/ataleoftwoqueues
l, r = map(int, input().split())
lq = sum([int(x) for x in input().split()])
lr = sum([int(x) for x in input().split()])
print("left" if lq < lr else "right" if lr < lq else "either")