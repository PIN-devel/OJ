import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def bfs():
    Q=deque()
    visit=[[False]*M for _ in range(N)]
    Q.append((C,R,0))
    visit[R][C]=True
    cnt=0
    while Q:
        x,y,depth=Q.popleft()
        if depth==L:break
        cnt += 1
        for d in pipe[mapBasement[y][x]]:
            nx,ny=x+dr[d][0],y+dr[d][1]
            if 0<=nx<M and 0<=ny<N and not visit[ny][nx] and (d+2)%4 in pipe[mapBasement[ny][nx]]:
                Q.append((nx,ny,depth+1))
                visit[ny][nx] = True


    return cnt
T = int(input())
pipe = [[], [0, 1, 2, 3], [0, 2], [1, 3], [0, 1], [1, 2], [2, 3], [0, 3]]
dr = [(0, -1), (1, 0), (0, 1), (-1, 0)]
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    mapBasement = [list(map(int, input().split())) for _ in range(N)]
    print("#{} {}".format(tc,bfs()))
