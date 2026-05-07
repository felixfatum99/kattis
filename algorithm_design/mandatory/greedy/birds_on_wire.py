import math

def boaw():
    l, d, n = map(int, input().split(" "))
    birds = []

    if n == 0:
        sum = 1
        min = 6
        while True:
            if min+d <= l-6:
                min += d
                sum+= 1
            else:
                break
        print(sum)
    else:
        for i in range(n):
            birds.append(int(input()))
        
        birds.sort()
        print(check_below(birds[0], d)+check_above(birds[n-1], d, l)+check_birds_interval(birds, d))

def check_below(high, space):
    sum = 0
    min = 6
    cp = high
    while True:
        if cp-space >= min:
            cp-=space
            sum+=1
        else:
            break
    return sum

def check_above(low, space, l):
    sum = 0
    max = l-6
    cp = low
    while True:
        if cp+space <= max:
            sum+=1
            cp += space
        else:
            break
    return sum

def check_birds_interval(birds, space):
    b = birds
    min = b.pop(0)
    sum = 0
    while b:
        next = b.pop(0)
        if next-(space*2) >= min:
            diff = math.floor((next-min)/space)
            sum+=diff-1
        min = next
    return sum

boaw()

