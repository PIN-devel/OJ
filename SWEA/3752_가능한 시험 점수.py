n,m,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[[] for _ in range(n)]
for i in range(n):
    for j in range(m):
        c[i].append(a[i]*b[j])
target=[1]
for e in range(2,k):
    if k%e==0:
        target.append(e)
target+=[k]
for i in c:
    print(i,target)