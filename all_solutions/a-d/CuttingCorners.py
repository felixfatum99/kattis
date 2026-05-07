import math
H, W = map(int, input().split())
diagonal = math.sqrt(pow(H, 2) + pow(W, 2))
square = H+W
print(square-diagonal)