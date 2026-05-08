#https://open.kattis.com/problems/butiwanttowin
a = int(input())

votes = sorted([int(x) for x in input().split()])
first = votes[len(votes)-1]
second = votes[len(votes)-2]

output = False
rounds = 0
for v in votes:
    if first+second == sum(votes):
        if second > first:
            output = True
        break
    elif first > sum(votes) * 0.5:
        break
    elif second > sum(votes) * 0.5:
        output = True
        break
    else:
        second += v
        rounds+=1

if output:
    print(rounds)
else:
    print("IMPOSSIBLE TO WIN")