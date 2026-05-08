line_1 = input().strip()
line_2 = input().strip()
line_3 = input().strip()
if line_1 == "O O O":
    print("Abdullah har vunnit")
elif line_1 == "X X X":
    print("Johan har vunnit")
elif line_2 == "O O O":
    print("Abdullah har vunnit")
elif line_2 == "X X X":
    print("Johan har vunnit")
elif line_3 == "O O O":
    print("Abdullah har vunnit")
elif line_3 == "X X X":
    print("Johan har vunnit")
elif line_1[0] == "O" and line_2[0] == "O" and line_3[0] == "O":
    print("Abdullah har vunnit")
elif line_1[2] == "O" and line_2[2] == "O" and line_3[2] == "O":
    print("Abdullah har vunnit")
elif line_1[4] == "O" and line_2[4] == "O" and line_3[4] == "O":
    print("Abdullah har vunnit")
elif line_1[0] == "O" and line_2[2] == "O" and line_3[4] == "O":
    print("Abdullah har vunnit")
elif line_1[4] == "O" and line_2[2] == "O" and line_3[0] == "O":
    print("Abdullah har vunnit")
elif line_1[0] == "X" and line_2[0] == "X" and line_3[0] == "X":
    print("Johan har vunnit")
elif line_1[2] == "X" and line_2[2] == "X" and line_3[2] == "X":
    print("Johan har vunnit")
elif line_1[4] == "X" and line_2[4] == "X" and line_3[4] == "X":
    print("Johan har vunnit")
elif line_1[0] == "X" and line_2[2] == "X" and line_3[4] == "X":
    print("Johan har vunnit")
elif line_1[4] == "X" and line_2[2] == "X" and line_3[0] == "X":
    print("Johan har vunnit")
else:
    print("ingen har vunnit")