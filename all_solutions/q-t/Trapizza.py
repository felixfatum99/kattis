import math
math.pi
ares_circel = math.pi * ((int(input())/2)**2)

l1 = int(input())
l2 = int(input())
height = int(input())

area_trapez = 0.5 * (l1+l2) * height

print("Trapizza!" if area_trapez > ares_circel else "Mahjong!" if ares_circel > area_trapez else "Jafn storar!")