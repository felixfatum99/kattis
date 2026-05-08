#https://open.kattis.com/problems/attemptedalphabet
word = ""
line = input()

for i in range(97, 123, 1):
    if chr(i) not in line:
        word+=chr(i)

print(word if word != "" else "Good job!")