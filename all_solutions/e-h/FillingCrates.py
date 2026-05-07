x = int(input())

impossible = {1, 2, 3, 5, 7, 11}

if x in impossible:
    print("impossible")

else:
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            print(f"{i}x{x//i}")
            break
    else:
        if x % 2 == 0:
            print(f"2x{x//2}")
        elif x >= 13:
            if x % 2 == 1:
                print(f"3x3 2x{(x-9)//2}")
            else:
                print(f"2x2 2x{(x-4)//2}")  
