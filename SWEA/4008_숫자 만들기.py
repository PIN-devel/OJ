from collections import deque


def getMinMax(k, n):
    if k == n:
        global Min,Max
        numCopy=deque()
        numCopy.extend(num)
        orderCopy=order[:]
        cal=numCopy.popleft()
        while orderCopy:
            o=orderCopy.pop()
            m=numCopy.popleft()
            if o=='+':
                cal+=m
            elif o=='-':
                cal-=m
            elif o=='*':
                cal*=m
            else:
                cal/=m
                cal=int(cal)
        if cal<Min:
            Min=cal
        if cal>Max:
            Max=cal

        return Min,Max

    for i in range(4):
        if not tmp[i]: continue

        tmp[i] -= 1
        order.append(OP[i])

        getMinMax(k + 1, n)

        tmp[i] += 1
        order.pop()


T= int(input())
OP="+-*/"
for tc in range(1,T+1):
    N=int(input())
    tmp=list(map(int,input().split()))
    n=sum(tmp)
    num=deque()
    num.extend(map(int,input().split()))
    order=[]
    Min, Max = 100000000, -100000000
    getMinMax(0, n)
    print('#{} {}'.format(tc, Max-Min))