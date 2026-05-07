def run():
    w = input()
    with_y = 0
    without_y = 0

    for l in w: 
        if l == "a" or l == "e" or l == "i" or l == "o" or l == "u":
            without_y += 1
            with_y += 1    
        if l == "y":
            with_y += 1

    print(without_y, with_y)
run()