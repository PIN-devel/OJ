# n=4
# arr=[1,2,1,2]
# result=[]
# for i in range(1<<n):
#     result = []
#     for j in range(n):
#         if i&(1<<j):
#             result.append(arr[j])
#     print(result)
def find_sum_K(lst):
    cnt = 0
    for i in range(1 << N):
        value = 0
        for j in range(N):
            if value > K: break
            if i & (1 << j):
                value += (lst[j])
        if value == K:
            cnt += 1
    return cnt


for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    data = list(map(int, input().split()))
    print('#{} {}'.format(tc, find_sum_K(data)))
def function(k):
    if ????
    (a)
    function(k+1)
    (b)
    function(k + 1)
    (c)