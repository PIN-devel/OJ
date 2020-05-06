T=int(input())
for tc in range(1,T+1):
    s=input()
    N=len(s)
    result="Exist"
    for i in range(N>>1):
        if(s[i]!=s[N-1-i]):
            if (s[i]=='?'or s[N-1-i]=='?'):continue
            result="Not Exist"
            break
    print("#{} {}".format(tc,result))