a, b = map(int, input().split())
lib = []
for i in range(a):
    bo, au = map(str, input().split(", "))
    lib.append((bo, au))

lib_sorted = sorted(lib, key=lambda element: (element[1], element[0]))

d = {}
for i in range(a):
    d[lib_sorted[i][0]] = i+1

for j in range(b):
    look = input()
    print(d[look] if look in d else -1)

