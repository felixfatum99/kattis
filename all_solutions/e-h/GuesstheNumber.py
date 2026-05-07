
bottom = 0
top = 1000
guess = 500
guessed = False
amount = 0
while not guessed and amount <= 9:
    print(guess, flush=True)
    amount += 1
    answer = input().strip()
    if answer == "lower":
        top = guess
        diff = top-bottom
        guess = int(guess-((diff-(diff%2))/2))
    elif answer == "higher":
        bottom = guess
        diff = top-bottom
        guess = int(guess+((diff+(diff%2))/2))
    elif answer == "correct":
        guessed = True


