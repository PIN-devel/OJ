def f(s, count, state):
    if s == N:
        global result
        if state == 'R' and count < result:
            result = count
        return
    if s == N - 1 and state == 'W':
        return

    if state == 'W':
        f(s + 1, count + M - flag[s].count('W'), 'W')
        f(s + 1, count + M - flag[s].count('B'), 'B')
    elif state == 'B':
        f(s + 1, count + M - flag[s].count('B'), 'B')
        f(s + 1, count + M - flag[s].count('R'), 'R')
    else:
        f(s + 1, count + M - flag[s].count('R'), 'R')


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]
    cnt = 0
    result = N * M
    for e in flag[0]:
        if e != 'W':
            cnt += 1
    f(1, cnt, 'W')
    print("#{} {}".format(tc, result))
