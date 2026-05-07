import bisect

while True:
    n = int(input())
    if n == 0:
        break
    
    d = {}
    names_sorted = []
    
    for i in range(n):
        name = input()
        sort_name = name[0]+name[1]
        if sort_name in d.keys():
            d[sort_name].append(name)
        else:
            d[sort_name] = [name]
        names_sorted.append(sort_name)
    
    names_sorted.sort()
    for ln in names_sorted:
        print(d[ln].pop(0))
    print()