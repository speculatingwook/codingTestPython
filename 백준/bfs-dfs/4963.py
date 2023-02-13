import sys
from typing import List

sys.setrecursionlimit(10000)


def data_input() -> (int, int, List[int]):
    width, height = map(int, input().split())
    if width == 0 and height == 0:
        return 0, 0, []
    map_list = []
    for i in range(height):
        width_line = list(map(int, input().split()))
        map_list.append(width_line)

    return width, height, map_list


def solution():
    def dfs(x, y):
        dx = [1, 1, -1, -1, 1, -1, 0, 0]
        dy = [0, 1, 0, 1, -1, -1, 1, -1]

        field[x][y] = 0
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < height and 0 <= ny < width and field[nx][ny] == 1:
                dfs(nx, ny)

    while True:
        width, height, field = data_input()
        if width == 0 and height == 0 and len(field) == 0:
            break

        count = 0
        for i in range(height):
            for j in range(width):
                if field[i][j] == 1:
                    dfs(i, j)
                    count += 1
        print(count)


solution()
