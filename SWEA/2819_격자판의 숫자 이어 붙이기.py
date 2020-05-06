def f(i, j, k, num):
    if k == 7:
        target.add(num)
        return
    for di, dj in dr:
        ni, nj = i + di, j + dj
        if 0 <= ni < 4 and 0 <= nj < 4:
            f(ni, nj, k + 1, num * 10 + board[ni][nj])


T = int(input())
for tc in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(4)]
    dr = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    target = set()
    for i in range(4):
        for j in range(4):
            f(i, j, 1, board[i][j])
    print('#{} {}'.format(tc, len(target)))