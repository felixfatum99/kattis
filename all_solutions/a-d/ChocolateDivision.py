w, h = map(int, input().split())
moves = (w*h)-1
if moves == 0:
    print("Beata")
elif moves == 1:
    print("Alf")
elif moves % 2 == 0:
    print("Beata")
else:
    print("Alf")