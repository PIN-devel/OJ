T=int(input())
for tc in range(1,T+1):
    W,H,N=map(int,input().split())
    x1,y1=map(int,input().split())
    result=0
    for _ in range(N-1):
        x2,y2=map(int,input().split())
        dx,dy=abs(x2-x1),abs(y2-y1)
        if(x1>x2 and y1<y2) or (x1<x2 and y1>y2):result+=dx+dy
        else:result+=dy if dy>dx else dx
        x1,y1=x2,y2
    print("#{} {}".format(tc,result))
