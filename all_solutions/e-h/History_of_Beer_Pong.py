n = int(input())

prev_a, prev_b = 10, 10
prev_turn = ""
inv = False
fin = False

for i in range(n):
    a, b = map(int, input().split())
    if i == 0: #first throw
        if prev_a - a >= 2 or prev_b - b >= 2 or (prev_a - a == 1 and prev_b - b == 1):
            inv = True
        elif a > prev_a or b > prev_b:
            inv = True
        else:
            if prev_a != a:
                prev_a = a
                prev_turn = "a"
            elif prev_b != b:
                prev_b = b
                prev_turn = "b"
    else:
        current_turn = ""
        if (prev_a != a and prev_b != b) or prev_a == 0 or prev_b == 0:
            inv = True
        elif prev_a != a:
            current_turn = "a"
        elif prev_b != b:
            current_turn = "b"
        else:
            if prev_turn == "a":
                current_turn = "b"
            elif prev_turn == "b":
                current_turn = "a"
        
        if current_turn == prev_turn:
            inv = True

        #TURN TAKING CORRECT AT THIS POINT AND GAMES SHOULDNT HAVE FINISHED

        #INVALID IF YOU SCORE MORE THAN 2 POINTS
        if prev_a - a > 2 or prev_b-b > 2:
            inv = True
        #INVALID IF YOU GO UP IN POINTS
        elif a > prev_a or b > prev_b:
            inv = True
        
        if prev_a != a:
            prev_a = a
            prev_turn = "a"
            if a == 0:
                fin = True
        elif prev_b != b:
            prev_b = b
            prev_turn = "b"
            if b == 0:
                fin = True
        elif prev_a == a and prev_b == b:
            if current_turn == "a":
                prev_turn = "a"
            elif current_turn == "b":
                prev_turn = "b"

if inv:
    print("invalid")
elif fin:
    print("finished")
else:
    print("ongoing")
        

        
