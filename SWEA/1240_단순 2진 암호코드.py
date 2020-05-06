import sys

sys.stdin = open('../input.txt', 'r')


def decode(target):
    tmp_sum = 0
    for k in range(5):
        tmp_sum += (1 << k) * target[k]
    return dict_decode[tmp_sum]


def check(final_code):
    check_value = 0
    for i in range(8):
        if i % 2:
            check_value += final_code[i]
        else:
            check_value += 3 * final_code[i]
    if check_value % 10:
        return False
    else:
        return True


dict_decode = {
    12: 0,
    6: 1,
    18: 2,
    15: 3,
    17: 4,
    3: 5,
    29: 6,
    23: 7,
    27: 8,
    20: 9,
}

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    code_bin = 0
    for _ in range(N):
        tmp = list(map(int, input()))
        if not code_bin and any(tmp):
            code_bin = tmp
    for i in range(-1, -100, -1):
        if code_bin[i]:
            code = []
            for j in range(-54, 0, 7):
                code.append(decode(code_bin[i + j:i + j + 5]))
            break
    if check(code):
        result = sum(code)
    else:
        result = 0
    print('#{} {}'.format(tc, result))
