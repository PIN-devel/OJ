import sys
sys.stdin=open('../input.txt','r')

hex_to_bit = {
    '0':'0000',
    '1':'0001',
    '2':'0010',
    '3':'0011',
    '4':'0100',
    '5':'0101',
    '6':'0110',
    '7':'0111',
    '8':'1000',
    '9':'1001',
    'A':'1010',
    'B':'1011',
    'C':'1100',
    'D':'1101',
    'E':'1110',
    'F':'1111',
}

pattern=[[[[-1]*5 for _ in range(5)] for _ in range(5)]for _ in range(5)]
pattern[3][2][1][1]=0
pattern[2][2][2][1]=1
pattern[2][1][2][2]=2
pattern[1][4][1][1]=3
pattern[1][1][3][2]=4
pattern[1][2][3][1]=5
pattern[1][1][1][4]=6
pattern[1][3][1][2]=7
pattern[1][2][1][3]=8
pattern[3][1][1][2]=9

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    D = [input() for _ in range(N)]
    print(D)