#https://open.kattis.com/problems/atlantis
import heapq

n = int(input())
stores = []
for i in range(n):
    nk = [int(x) for x in input().split()]
    stores.append((nk[0], nk[1]))

stores.sort(key=lambda x: x[1])
pq = []
st = []  
s = 0

for store in stores:
    heapq.heappush(pq, -store[0])  
    s += store[0]

    while s > store[1]:
        t = -heapq.heappop(pq)
        s -= t
    
    st.append(store)
print(len(pq))