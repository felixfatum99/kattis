#https://open.kattis.com/problems/attendance2
callouts = int(input())
absentees = []

prev_name = ""
for _ in range(callouts):
    call = input()
    if call == "Present!":
        prev_name = ""
    else:
        if prev_name != "":
            absentees.append(prev_name)
            prev_name = call
        else:
            prev_name = call

if prev_name != "":
    absentees.append(prev_name)

if absentees:
    for a in absentees:
        print(a)
else:
    print("No Absences")