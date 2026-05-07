c = int(input())
line = input()

jumps = 0
current = 0
end = len(line)
answer = ""

while(jumps<c):
    red = False
    blue = False
    green = False
    for i in range(current, end):
        if (red and blue and not green and line[i] == "G"):
            jumps+=1
            answer+="G"
            current = i+1
            break
        elif (green and blue and not red and line[i] == "R"):
            jumps+=1
            answer+="R"
            current = i+1
            break
        elif (red and green and not blue and line[i] == "B"):
            jumps+=1
            answer+="B"
            current = i+1
            break
        else:
            if line[i] == "R":
                red = True
            elif line[i] == "B":
                blue = True
            else:
                green = True

print(answer)           