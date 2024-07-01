import heapq
n = int(input())
# Give input 2D matrix size of n
l = [list(map(int,input().split())) for i in range(n)]
x = int(input())
c = [False]*n
p = [[x] for i in range(n)]
q = [(0,x)]
d = [float('inf')]*n

while q:
    dist,node = heapq.heappop(q)
    c[node-1]=True
    for i in range(n):
        if l[node-1][i]!=0 and not c[i]:
            e = l[node-1][i]+dist
            if e<d[i]:
                d[i]=e
                p[i]=p[node-1]+[i+1]
                heapq.heappush(q,(e,i+1))
d[x-1]=0
for i in range(n):
    print(d[i])
    print(p[i])
