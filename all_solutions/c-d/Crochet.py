cal = {
    "Mon": 0,
    "Tue": 1,
    "Wed": 2,
    "Thu": 3,
    "Fri": 4,
    "Sat": 5,
    "Sun": 6
}

cal_inv = {
    0: "Mon",
    1: "Tue",
    2: "Wed",
    3: "Thu",
    4: "Fri",
    5: "Sat",
    6: "Sun"
}

day1, time1 = input().split()
day2, time2 = input().split()
hour1, minute1 = time1.split(":")
hour2, minute2 = time2.split(":")
hour1 = int(hour1) 
minute1 = int(minute1)
hour2 = int(hour2) 
minute2 = int(minute2)

final_minutes = 0
final_hours = 0
final_days = 0

if minute1 > minute2:
    final_minutes += (60-minute1) + minute2
    hour1+=1
elif minute2 > minute1:
    final_minutes += minute2 - minute1

if hour1 > hour2:
    final_hours += (24-hour1) + hour2
    day1 = cal_inv[(cal[day1]+1) % 7]
elif hour2 > hour1:
    final_hours += hour2 - hour1

if cal[day1] > cal[day2]:
    final_days += 7-cal[day1]+cal[day2]
elif cal[day2] > cal[day1]:
    final_days += cal[day2] - cal[day1]

components = 0
if final_days > 0:
    components+=1
if final_hours > 0:
    components+=1
if final_minutes > 0:
    components += 1

final_string = ""
if final_days > 0:
    final_string += str(final_days) + " day" if final_days == 1 else str(final_days) + " days"

if final_hours > 0:
    if final_string != "":
        final_string += ", " if components == 3 else " and "
    final_string += str(final_hours) + " hour" if final_hours == 1 else str(final_hours) + " hours"

if final_minutes > 0:
    if final_string != "":
        final_string += ", " if components == 3 else " and "
    final_string += str(final_minutes) + " minute" if final_minutes == 1 else str(final_minutes)+ " minutes"

print(final_string if final_string != "" else "7 days")