def hear():
    a = input()
    b = input()
    output = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            output += 1
    
    print(output+1)
hear()