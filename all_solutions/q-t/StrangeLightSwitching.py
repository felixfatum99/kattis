import heapq as h
p,q=h.heappush,h.heappop;z=input
n=int(z());a=sorted(map(int,z().split()))
m=a[1:];h.heapify(m);l=[-a[0]]
for _ in range((n-3)//2):
 c=m[0];print(c);x,y=map(int,z().split())
 if x>c<y:p(m,x);p(m,y);p(l,-q(m))
 elif x<c>y:p(l,-x);p(l,-y);p(m,-q(l))
 else:p(m,max(x,y));p(l,-min(x,y))
print(m[0])