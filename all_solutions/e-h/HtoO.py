line, amount = map(str, input().split())
final_line = input()
amount = int(amount)
molecules = {}
final_molecules = {}

has_letter = False
current_letter = ""
current_amount = ""
for c in line:
    if has_letter:
        if ord(c) > 47 and ord(c) < 58:
            current_amount+=c
        elif ord(c) > 58:
            if current_letter in molecules.keys():
                molecules[current_letter] += int(current_amount)*amount if current_amount != "" else amount
            else:
                molecules[current_letter] = int(current_amount)*amount if current_amount != "" else amount
            current_letter = c
            current_amount = ""
    else:
        current_letter = c
        has_letter = True
if current_letter in molecules.keys():
    molecules[current_letter] += int(current_amount)*amount if current_amount != "" else amount
else:
    molecules[current_letter] = int(current_amount)*amount if current_amount != "" else amount

has_letter = False
current_letter = ""
current_amount = ""
for c in final_line:
    if has_letter:
        if ord(c) > 47 and ord(c) < 58:
            current_amount+=c
        elif ord(c) > 58:
            if current_letter in final_molecules.keys():
                final_molecules[current_letter] += int(current_amount) if current_amount != "" else 1
            else:
                final_molecules[current_letter] = int(current_amount) if current_amount != "" else 1
            current_letter = c
            current_amount = ""
    else:
        current_letter = c
        has_letter = True

if current_letter in final_molecules.keys():
    final_molecules[current_letter] += int(current_amount) if current_amount != "" else 1
else:
    final_molecules[current_letter] = int(current_amount) if current_amount != "" else 1


can_build = True
smallest_c_d = float('inf')
for k in final_molecules:
    if k in molecules.keys():
        smallest_c_d = min(smallest_c_d, (molecules[k]//final_molecules[k]))
    else:
        can_build = False
        break

if can_build:
    print(smallest_c_d)
else:
    print(0)

