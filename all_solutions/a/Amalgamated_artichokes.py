#https://open.kattis.com/problems/artichoke
import math

def run(): 
    list= input()
    res = [int(x) for x in list.split(" ")]
    mini = float(0)
    maxi = float(0)
    output = float(0)

    for x in range(res[5]):
        p = res[0]*(math.sin(res[1]*(x+1)+res[2])+math.cos(res[3]*(x+1)+res[4])+2)
        if(x==0):
            mini = p
            maxi = p
        else:
            mini = min(mini, p)
            if max(maxi, p) != maxi:
                mini = max(maxi, p)
            maxi = max(maxi, p)
            output = max((maxi-mini),output)
    
    print(output)
run()