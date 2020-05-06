T=int(input())
for tc in range(1,T+1):
    N= int(input())
    result=-1
    pivotMax=1000000 #10^6
    pivotMin=1
    if N!=1 and N!=1000000000000000000:
        while pivotMax-pivotMin!=1:
            pivot=(pivotMax+pivotMin)>>1
            sqPivot=pivot*pivot*pivot
            if sqPivot<N:
                pivotMin=(pivotMax+pivotMin)>>1
            elif sqPivot>N:
                pivotMax=(pivotMax+pivotMin)>>1
            else:
                result=pivot
                break
    elif N==1:result=1
    else:result=pivotMax
    print('#{} {}'.format(tc,result))