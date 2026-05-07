def p():
    x = input().split(" ")
    x[0] = int(x[0])
    x[1] = int(x[1])
    matrix = []
    output = "Neibb"

    for i in range(x[0]):
        p = [int(x) for x in input().split(" ", -1)]
        matrix.append(p)
    
    for i in range(1, x[0]-1):
        for j in range(1, x[1]-1):
            if matrix[i][j] < matrix[i-1][j] and matrix[i][j] < matrix[i+1][j] and matrix[i][j] < matrix[i][j-1] and matrix[i][j] < matrix[i][j+1]:
                output = "Jebb"
    
    print(output)

p()