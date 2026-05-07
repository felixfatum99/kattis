while True:
    m = int(input())
    
    if m == 0:
        break
    
    q1 = 0
    q2 = 0

    for _ in range(m):
        c, a = input().split()
        a = int(a)
        if c == 'DROP':
            print('DROP 1', a)
            q1 += int(a)
        elif c == 'TAKE':
            if q2 >= a:
                print('TAKE 2', a)
                q2 -= a
            elif q2 < a and q2 > 0:
                print('TAKE 2', q2)
                print('MOVE 1->2', q1)
                print('TAKE 2', a-q2)
                q2 = q1 - (a - q2)
                q1 = 0
            elif q2 == 0:
                print('MOVE 1->2', q1)
                q2 = q1
                q1 = 0
                print('TAKE 2', a)
                q2 -= a
    print()