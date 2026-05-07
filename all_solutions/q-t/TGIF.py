cal = {
    "JAN": 31,
    "FEB": 28,
    "MAR": 31,
    "APR": 30,
    "MAY": 31,
    "JUN": 30,
    "JUL": 31,
    "AUG": 31,
    "SEP": 30,
    "OCT": 31,
    "NOV": 30,
    "DEC": 31,
}

cal2 = {
    "JAN": 1,
    "FEB": 2,
    "MAR": 3,
    "APR": 4,
    "MAY": 5,
    "JUN": 6,
    "JUL": 7,
    "AUG": 8,
    "SEP": 9,
    "OCT": 10,
    "NOV": 11,
    "DEC": 12,
}

cal3 = {
    "MON": 0,
    "TUE": 1,
    "WED": 2,
    "THU": 3,
    "FRI": 4,
    "SAT": 5,
    "SUN": 6
}

cal4 = {
    0: "MON",
    1: "TUE",
    2: "WED",
    3: "THU",
    4: "FRI",
    5: "SAT",
    6: "SUN"
}

months = ["JAN","FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

day, month = map(str, input().split())
start_day = input()
day = int(day)

total_days = day-1
for h in range(12):
    if months[h] == month:
        break
    total_days+=cal[months[h]]

days_after_start_day = total_days % 7

if month == "JAN" or month == "FEB":
    if cal4[(cal3[start_day]+days_after_start_day) % 7] == "FRI":
        print("TGIF")
    else:
        print(":(")
else:
    if cal4[(cal3[start_day]+days_after_start_day) % 7] == "FRI" or cal4[(cal3[start_day]+days_after_start_day+1) % 7] == "FRI":
        print("not sure")
    else:
        print(":(")



