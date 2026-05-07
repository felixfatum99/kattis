def run():
    x_1_y_1 = input().split(" ")
    x_2_y_2 = input().split(" ")
    x_3_y_3 = input().split(" ")

    a = area(int(x_1_y_1[0]), int(x_1_y_1[1]), int(x_2_y_2[0]), int(x_2_y_2[1]), int(x_3_y_3[0]), int(x_3_y_3[1]))

    x = int(input())

    output = 0
    for i in range(x):
        p = input().split(" ")
        b = isInside(int(x_1_y_1[0]), int(x_1_y_1[1]), int(x_2_y_2[0]), int(x_2_y_2[1]), int(x_3_y_3[0]), int(x_3_y_3[1]), int(p[0]), int(p[1]))
        if b:
            output += 1
    
    print(a)
    print(output)

def area(x1, y1, x2, y2, x3, y3):
 
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) 
                + x3 * (y1 - y2)) / 2.0)
 

def isInside(x1, y1, x2, y2, x3, y3, x, y):
 
    # Calculate area of triangle ABC
    A = area (x1, y1, x2, y2, x3, y3)
 
    # Calculate area of triangle PBC 
    A1 = area (x, y, x2, y2, x3, y3)
     
    # Calculate area of triangle PAC 
    A2 = area (x1, y1, x, y, x3, y3)
     
    # Calculate area of triangle PAB 
    A3 = area (x1, y1, x2, y2, x, y)
     
    # Check if sum of A1, A2 and A3 
    # is same as A
    if(A == A1 + A2 + A3):
        return True
    else:
        return False

run()