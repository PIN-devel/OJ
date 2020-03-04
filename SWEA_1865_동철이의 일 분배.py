
def sumP(k, s):
    if k == N:
        global maxV
        if maxV < s:
            maxV = s
        return
    for i in range(N):
        if not worked[i]:
            if s > maxV:
                worked[i] = True
                sumP(k + 1, s * P[k][i] * 0.01)
                worked[i] = False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    maxV = -1
    worked = [False] * N
    sumP(0, 1)
    print('#%d %.6f' % (tc, maxV * 100))
