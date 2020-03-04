import sys
sys.stdin=open('input.txt','r')

def moveTernal(k):
    pass

T = int(input())

for tc in range(1, T + 1):
    N,M,R,C,L=map(int,input().split())
    ternal=[list(map(int,input().split()) for _ in range(N))]
