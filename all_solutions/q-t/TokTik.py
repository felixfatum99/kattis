
def tiktok():
    i = int(input())
    d = dict()

    for x in range(i):
        line = input().split(" ")
        if d.__contains__(line[0]):
            d[line[0]] = d.get(line[0])+int(line[1])
        else:
            d[line[0]] = int(line[1])

    output = ""
    score = 0
    for item in d:
        if d.get(item) > score:
            output = item
            score = d.get(item)
    
    print(output)
tiktok()
