T=int(input())
for tc in range(1,T+1):
    bar=input()
    numBar=0
    result=0
    preBar=bar[0]
    for e in bar:
        if e=='(':
            numBar+=1
        else:
            numBar -= 1
            if preBar=='(':
                result+=numBar
            else:
                result+=1
        preBar=e

    print('#{} {}'.format(tc,result))
