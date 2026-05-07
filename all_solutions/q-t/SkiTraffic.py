def calc(hour, minute, multiplier):
    final_hours = hour * multiplier
    final_minutes = (minute * multiplier) % 60
    final_hours += ((minute * multiplier) - (final_minutes)) / 60

    return [int(final_hours), int(final_minutes)]

input()
hour, minute = map(int, input().split(":"))
hour, minute = map(int, calc(hour, minute, 2) if input() in ["sat", "sun"] else [hour, minute])
hour, minute = map(int, calc(hour, minute, 2) if int(input()) == 1 else [hour, minute])
hour, minute = map(int, calc(hour, minute, 3) if int(input()) == 1 else [hour, minute])
hour, minute = map(int, calc(hour, minute, 3) if int(input()) == 1 else [hour, minute])

if minute < 10:
    minute = "0"+str(minute)

print(str(hour)+":"+str(minute))


