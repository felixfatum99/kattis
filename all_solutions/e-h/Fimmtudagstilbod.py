def run():
    inp = int(input())
    output = 1000
    if inp < 2021:
        print(output)
    else:
        print(output+((inp-2020)*100))
run()