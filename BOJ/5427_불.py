import sys


def find_start():
    for i in range(w):
        for j in range(h):
            if building[j][i] == '@':
                return i, j


def update_fire(f):
    global building
    new_fire = []
    while f:
        x, y = f.pop()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h and building[ny][nx] == '.':
                building[ny][nx] = '*'
                new_fire.append((nx, ny))
    return new_fire


def find_fire():
    global fire
    for i in range(w):
        for j in range(h):
            if building[j][i] == '*':
                fire.append((i, j))


sys.stdin = open("D:/Documents/code/OJ/input.txt", "r")

T = int(input())
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for tc in range(1, T + 1):
    w, h = map(int, input().split())
    building = [list(input()) for _ in range(h)]
    x, y = find_start()
    fire = []
    for i in building:
        print(i)
    find_fire()
    fire = update_fire(fire)
    fire = update_fire(fire)
    for i in building:
        print(i)
