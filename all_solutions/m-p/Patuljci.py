dwarves = []

for i in range(9):
    dwarves.append(int(input()))

found = False

def rec(acc_sum, index, selected):
    global found
    if found:
        return
    if len(selected) == 7 and acc_sum == 100:
        found = True
        selected.sort()
        for idx in selected:
            print(dwarves[idx])
        return
    if len(selected) > 7 or index >= 9:
        return
    
    rec(acc_sum, index + 1, selected)
    
    rec(acc_sum + dwarves[index], index + 1, selected + [index])

rec(0, 0, [])
