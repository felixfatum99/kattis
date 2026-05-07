t, n = map(int, input().split())
songs = [int(x) for x in input().split()]
songs.sort()
ct = 0
t = 60*t

for i in range(len(songs)):
    if ct+songs[i]<=t:
        ct+=songs[i]
    else:
        break

print(ct)
