def DFS(s,i,j):
    for w in range(N):
        if G[i][w] and not visit[w]:
            visit[w] = True
            DFS(s,w,j)
            if visit[j]:
                result[s][j] = 1
                return


N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
result = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        visit = [False] * N
        DFS(i,i,j)
for e in result:
    print(*e)