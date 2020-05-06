from collections import deque


def BFS(s):
    global result
    Q = deque()
    Q.append((s, 1))
    visit = [False] * (N + 1)
    visit[s] = True
    while Q:
        x, d = Q.popleft()
        if d > result:
            result = d
        for w in G[x]:
            if not visit[w]:
                visit[w] = True
                Q.append((w, d + 1))
                visit[w] = False


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    result = -1
    for i in range(1, N + 1):
        BFS(i)
    print("#{} {}".format(tc, result))
