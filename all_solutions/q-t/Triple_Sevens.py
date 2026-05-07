def run():
    n = int(input())
    output = 777
    for i in range(3):
        a = input().split(" ")
        temp_output = False
        for j in range(n):
            if a[j] == '7':
                temp_output = True
        if temp_output is False:
            output = 0
    
    print(output)

run()