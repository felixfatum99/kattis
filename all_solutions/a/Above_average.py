#https://open.kattis.com/problems/aboveaverage
for _ in range(int(input())):
    nums = list(map(int, input().split()))
    
    n = nums[0]
    scores = nums[1:]
    
    avg = sum(scores) / n
    above = sum(score > avg for score in scores)

    print(f"{above / n * 100:.3f}%")