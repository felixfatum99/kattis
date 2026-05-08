def run():
    i = int(input())

    for x in range(i):
        inp = input().split(" ")
        inp.pop(0)
        area(inp)

def area(p_array):
    first_product = 0
    second_product = 0

    for i in range(0, len(p_array), 2):
        if i == len(p_array)-2:
            first_product += int(p_array[i])*int(p_array[2])
            second_product += p_array[i+1]*p_array[0]
        else:
            first_product += p_array[i]*p_array[i+3]
            second_product += p_array[i+1]*p_array[i+2]
    
    result = 0.5*(first_product-second_product)
    print(result)
run()




