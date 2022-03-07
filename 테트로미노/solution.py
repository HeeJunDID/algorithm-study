import sys
from pprint import pprint

sys.stdin = open("./ex3.txt")
n, m = map(int, sys.stdin.readline().split())
n_map = []
for _ in range(n):
    n_map.append(list(map(int, sys.stdin.readline().split())))
v_map = [[False for _ in range(m)] for _ in range(n)]
pprint(v_map)
blocks = [
    [[0, 1], [0, 2], [0, 3]],
    [[1, 0], [2, 0], [3, 0]],
    [[0, 1], [1, 0], [1, 1]],
    # 8개 나와야됨
    [[1, 0], [2, 0], [2, 1]],
    [[1, 0], [2, 0], [2, -1]],
    [[0, 1], [1, 0], [2, 0]],
    [[0, 1], [1, 1], [2, 1]],
    [[1, 0], [1, 1], [1, 2]],
    [[1, 0], [1, -1], [1, -2]],
    [[0, 1], [0, 2], [1, 0]],
    [[0, 1], [0, 2], [1, 2]],
    # 4개
    [[1, 0], [1, 1], [2, 1]],
    [[1, 0], [1, -1], [2, -1]],
    [[0, 1], [1, 0], [1, -1]],
    [[0, 1], [1, 1], [1, 2]],
    # 4개
    [[0, 1], [1, 2], [1, 1]],
    [[1, 0], [1, 1], [1, -1]],
    [[1, 0], [2, 0], [1, 1]],
    [[1, 0], [2, 0], [1, -1]],
]
ans = 0
for i in range(n):
    for j in range(m):
        for block in blocks:
            state = True
            s = n_map[i][j]
            for dx, dy in block:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m:
                    s += n_map[x][y]
                else:
                    state = False
                    break
            if state and (ans < s):
                ans = s
print(ans)
