#https://open.kattis.com/problems/addingtrouble
a, b, c = map(int, input().split())
print("correct!" if a + b == c else "wrong!")