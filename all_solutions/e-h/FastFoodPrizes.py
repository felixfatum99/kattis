t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    prizes = {}
    prizes_arr = []
    for _ in range(n):
        prize = [int(x) for x in input().split()]
        r = prize[0]
        c = prize[r+1]
        prizes_arr.append(c)
        prizes[c] = prize[1:r+1]
    
    prizes_arr.sort(reverse=True)
    stickers = [int(s) for s in input().split()]
    
    output = 0

    for i in range(len(prizes_arr)):
        values = prizes[prizes_arr[i]]
        checker = True
        while checker:
            for j in range(len(values)):
                if stickers[values[j]-1] < 1:
                    checker = False
                    break
            if checker:
                for k in range(len(values)):
                    stickers[values[k]-1] -= 1
                output += prizes_arr[i]

    print(output)