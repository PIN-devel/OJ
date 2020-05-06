



T=int(input())
for tc in range(1,T+1):
    p,q=map(int,input().split())
    indenp=[0]*p #들여쓰기 온점 개수 기록

    codep=[]
    codeq=[]

    R,C,S=0,0,0
    for _ in range(p):
        codep.append((input()))
    for _ in range(q):
        codeq.append((input()))
    for i in range(p):
        cnt=0
        while codep[i][cnt]=='.':
            cnt+=1
        indenp[i]=cnt
    print(indenp)