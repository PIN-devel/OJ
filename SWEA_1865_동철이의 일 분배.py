def calP(k, s):
    global maxV
    if s <= maxV:
        return
    if k == N:
        if maxV < s:
            maxV = s
        return
    for i in range(N):
        if not worked[i]:
            worked[i] = True
            calP(k + 1, s * P[k][i])
            worked[i] = False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    P = [list(map(lambda x: float(x) * 0.01, input().split())) for _ in range(N)]
    maxV = -1
    worked = [False] * N
    calP(0, 1)
    print('#%d %.6f' % (tc, maxV * 100))
