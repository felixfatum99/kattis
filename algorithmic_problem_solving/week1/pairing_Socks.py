n = int(input())

s = [int(x) for x in input().split()]
a = []
moves = 0

while True:
    if not a:
        if not s:
            print(moves)
            break
        a.append(s.pop())
        moves += 1
    else:
        if not s:
            print("impossible")
            break

        sock_a = s.pop()
        sock_b = a.pop()

        if sock_a == sock_b:
            moves += 1
        else:
            a.append(sock_b)
            a.append(sock_a)
            moves += 1