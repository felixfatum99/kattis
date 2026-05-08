#https://open.kattis.com/problems/bladra2
import math

inp = input().split(" ")
v = int(inp[0])
a = int(inp[1])
t = int(inp[2])

d = (v*t)+0.5*(a*math.pow(t, 2))
print(d)