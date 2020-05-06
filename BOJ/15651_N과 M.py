###(4)###
def getSequence(s, k):
    if k == M:
        print(*result)
        return
    for i in range(s, N + 1):
        result.append(i)
        getSequence(i, k + 1)
        result.pop()


N, M = map(int, input().split())
result = []
getSequence(1, 0)

###(3)###
# def getSequence(k):
#     if k == M:
#         print(*result)
#         return
#     for i in range(1, N + 1):
#         result.append(i)
#         getSequence(k + 1)
#         result.pop()
#
#
# N, M = map(int, input().split())
# result = []
# getSequence(0)

####(2)####
# def getSequence(s, k):
#     if N - s + k + 1 < M:
#         return
#     if k == M:
#         print(*result)
#         return
#     for i in range(s, N + 1):
#         result.append(i)
#         getSequence(i + 1, k + 1)
#         result.pop()
#
#
# N, M = map(int, input().split())
# result = []
# getSequence(1, 0)

####(1)####
# def getSequence(k):
#     if k == M:
#         print(*result)
#         return
#     for i in range(1, N + 1):
#         if not used[i]:
#             result.append(i)
#             used[i] = True
#             getSequence(k + 1)
#             result.pop()
#             used[i] = False
#
#
# N, M = map(int, input().split())
# result = []
# used = [False] * (N + 1)
# getSequence(0)
