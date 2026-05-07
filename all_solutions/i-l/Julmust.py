n = int(input())
guessed = False

if n % 2 != 0:
    guess = int((n-1)/2)
else:
    guess = int(n/2)

bottom = 0
top = n
correct_value = 761203
day = 1
flag = False
flag_guess = 0
while not guessed:
    if top-bottom < 85-day and not flag:
        flag = True
        flag_guess = bottom
    
    if flag:
        print(flag_guess*day, flush=True)
        flag_guess+=1
        day+=1
        answer = input().strip()
        if answer == "exact":
            guessed = True
    else:
        print(guess*day, flush=True)
        answer = input().strip()
        day+=1
        if answer == "less":
            top = guess
            diff = top-bottom
            guess = int(bottom + ((diff-(diff%2))/2))
        elif answer == "more":
            bottom = guess
            diff = top-bottom
            guess = int(bottom + ((diff-(diff%2))/2))
        elif answer == "exact":
            guessed = True