line = input().split(" ")
if int(line[0]) == int(line[2]):
    print("Goggi svangur!")
elif int(line[0]) < int(line[2]):
    print("<")
else:
    print(">")