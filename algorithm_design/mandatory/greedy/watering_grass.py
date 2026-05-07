import math
import sys


def sprinkler():
    for line in sys.stdin:
        n, l, w = map(int, line.split(" "))
        
        sprinklers = []
        for i in range(n):
            x, r = map(int, input().split(" "))
            sprinkler_covering_distance = math.sqrt(pow(r, 2)-pow((w/2), 2))
            sprinklers.append((x-sprinkler_covering_distance, x+sprinkler_covering_distance))
        
        sprinklers.sort(key=lambda x: abs(x[0]))

        sum = 0
        

        for i in range(sprinkler_covering_distance):

