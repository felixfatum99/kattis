n = int(input())

order = []
order.remove
regents = {}
last_name_lookup = {}

for i in range(n):
    names = input().split()
    order.append(names[0])
    
    if names[0] in regents and len(regents[names[0]]) >= 1:
        regents[names[0]].append(len(regents[names[0]])+1)
    elif names[0] not in regents:
        regents[names[0]] = [1]
    if len(names) > 1:
        last_names = ""
        for i in range(1, len(names)):
            last_names += names[i]+" "
        if names[0] in last_name_lookup:
            last_name_lookup[names[0]].append(last_names)
        else:
            last_name_lookup[names[0]]= [last_names]
    else:
        if names[0] in last_name_lookup:
            last_name_lookup[names[0]].append("")
        else:
            last_name_lookup[names[0]] = [""]
            
for regent in order:
    number = str(regents[regent][0])+"." if (len(regents[regent]) > 1) or regents[regent][0] > 1 else ""
    regents[regent].remove(regents[regent][0])
    last_name = last_name_lookup[regent][0]
    last_name_lookup[regent].remove(last_name_lookup[regent][0])
    print(regent, number, last_name)


