def f(k, p):
    if k>= 12:
        global result
        if result > p:
            result = p
        return

    f(k + 1, p+price[k])

    f(k + 3, p+M3)


T = int(input())
for tc in range(1, T + 1):
    D, M, M3, Y = map(int, input().split())
    plan = list(map(int, input().split()))
    price = [x * D for x in plan]

    for i in range(12):
        if price[i] > M:
            price[i] = M

    result = Y

    f(0, 0)

    print('#{} {}'.format(tc, result))