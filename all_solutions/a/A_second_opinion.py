#https://open.kattis.com/problems/secondopinion
n = int(input())
sec = n%60 
n = n-sec   
min = (n/60)%60 
n = (n/60)-min
hours = n/60
print(int(hours), ":", int(min), ":", int(sec))
