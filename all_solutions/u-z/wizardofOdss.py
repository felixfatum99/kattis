a, b = map(int, input().split())

for i in range(b):
    a = (a+(a%2))/2

#print(a)

if a<=1:
    print("Your wish is granted!")
else:
    print("You will become a flying monkey!")