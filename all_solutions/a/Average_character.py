#https://open.kattis.com/problems/averagecharacter
import math
s = input()
sum = 0
for c in s:
    sum+=ord(c)
print(chr(math.floor(sum/len(s))))