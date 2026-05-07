seed, key = map(str, input().split())

iteration = 0

while True:
    temp = ""
    prev_c = ""
    counter = 0

    for c in seed:
        if prev_c == c or prev_c == "":
            counter+=1
            prev_c = c
        else:
            temp = temp + str(counter) + str(prev_c)
            counter = 1
            prev_c = c

    temp = temp + str(counter) + str(prev_c)
    iteration += 1
    seed = temp
    if seed == key:
        break

print(iteration)