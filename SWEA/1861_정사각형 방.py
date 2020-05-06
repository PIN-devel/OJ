T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    v = [0] * (N * N + 1)
    dr = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    resultDepth = 1

    for x in range(N):
        for y in range(N):
            for d in dr:
                nx, ny = x + d[0], y + d[1]
                if 0 <= nx < N and 0 <= ny < N and A[nx][ny] == A[x][y] + 1:
                    v[A[x][y]] = 1
                    break
    Depth = 1
    l = 1
    while l < len(v):
        if v[l]:
            Depth += 1
            l += 1
            if Depth > resultDepth:
                resultDepth = Depth
                resultNum = l-Depth+1
        else:
            Depth = 1
            l += 1

    print('#{} {} {}'.format(tc, resultNum, resultDepth))
