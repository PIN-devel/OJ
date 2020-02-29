from collections import deque


def BFS():
    Q = deque()
    Q.append((0, 0, 1, 0))
    visit = [[[False] * 2 for _ in range(M)] for _ in range(N)]

    while Q:
        x, y, d, wall = Q.popleft()
        visit[y][x][wall] = True
        if x == M - 1 and y == N - 1:
            return d
        for e in dr:
            nx, ny = x + e[0], y + e[1]
            if 0 <= nx < M and 0 <= ny < N and not visit[ny][nx][wall]:
                if not MAP[ny][nx] or (MAP[ny][nx] and not wall):
                    visit[ny][nx][wall] = True

                    if MAP[ny][nx]:
                        Q.append((nx, ny, d + 1, 1))
                    else:
                        Q.append((nx, ny, d + 1, wall))

    return -1


N, M = map(int, input().split())
MAP = [list(map(int, input())) for _ in range(N)]
dr = [(0, 1), (1, 0), (-1, 0), (0, -1)]
print(BFS())
