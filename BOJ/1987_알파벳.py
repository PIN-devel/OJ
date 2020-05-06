def DFS(x, y, d):
    global result
    visited[y][x] = True
    used[ord(board[y][x])] = True
    if d > result:
        result = d
    for dx, dy in dr:
        nx, ny = x + dx, y + dy
        if 0 <= nx < C and 0 <= ny < R and not visited[ny][nx] and not used[ord(board[ny][nx])]:
            DFS(nx, ny, d + 1)
            used[ord(board[ny][nx])]=False
            visited[ny][nx]=False


R, C = map(int, input().split())
board = [input() for _ in range(R)]
visited = [[False] * C for _ in range(R)]
dr = [(1, 0), (0, 1), (-1, 0), (0, -1)]
used = [False] * 91
result = 0
DFS(0,0,1)
print(result)