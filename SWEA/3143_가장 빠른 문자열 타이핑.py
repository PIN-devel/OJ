T=int(input())
for tc in range(1,T+1):
    A,B=input().split()
    N,M=len(A),len(B)
    # skip 테이블 생성
    skip = [M]*128 #a~z, A~Z
    for i in range(M-1):
        skip[ord(B[i])]=M-1-i
    i=0
    cnt=0
    while i<N-M+1:
        for j in range(M-1,-1,-1):
            if B[j]!=A[i+j]:
                i+=skip[ord(A[i+M-1])]
                break
        else:
            cnt+=1
            i+=M
    result=N-(M-1)*cnt
    print("#{} {}".format(tc,result))