a, b = map(str, input().split())
a = a.replace("2", "C").replace("5", "2").replace("C", "5")
b = b.replace("2", "C").replace("5", "2").replace("C", "5")
print(1 if int(a[::-1]) > int(b[::-1]) else 2)