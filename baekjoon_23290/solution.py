import sys
from pprint import pprint
from collections import deque
sys.stdin = open('./ex1.txt')
origin_loc = []
mat = [[[] for _ in range(4)] for _ in range(4)]
m, s = map(int,sys.stdin.readline().strip().split())

for _ in range(m):
    fx, fy, d = map(int, sys.stdin.readline().strip().split())
    fx, fy, d = fx-1, fy-1, d
    mat[fx][fy] = [(d,s)]
    origin_loc.append((fx,fy,d))
# pprint(mat)
# print(' ')
sx,sy = map(int, sys.stdin.readline().strip().split())
sx, sy = sx-1, sy-1
mat[sx][sy] = 's'
# pprint(mat)
# if sum(mat[0][2]) != 0:
#     mat[0][2].append(5)
# else:
#     mat[0][2] = 5
# print(sum(mat[0][2]))
# pprint(mat)
def change_direction(d):
    d -= 1
    if d == 0:
        d = 8
    return d


def fish_move(mat, fx, fy, d, s):
    """
    물고기 움직임 정의
    ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 
    1부터 순서대로 idx가짐
    """
    origin_d = str(d)
    dx = [0,0, -1, -1, -1, 0, 1, 1, 1]
    dy = [0,-1, -1, 0, 1, 1, 1, 0, -1]
    state = False
    cnt = 0
    while state == False:
        nx = fx + dx[d]
        ny = fy + dy[d]
        if 0<=nx<4 and 0<=ny<4 and ['s','ds'] not in mat[nx][ny]:
            if len(mat[nx][ny]) != 0:
                mat[nx][ny].append((d, s+1))
                state = True
            else:
                mat[nx][ny] = [(d, s+1)]
                state = True
        if cnt == 8:
            break
        else:
            change_direction(d)
            cnt += 1
    return mat

def shark_move(mat,sx,sy):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    queue = deque((mat,sx,sy))
    result = []
    eat_cnt = 0
    while queue:
        que = queue.popleft()
        for q in que:
            m, x, y = q
            for i in range(len(dx)):
                nx = x + dx[i]
                ny = y + dy[i]
            




for i in range(len(mat)):
    for j in range(len(mat)):
        # print(mat[i][j])
        # print(list(map(lambda x: x[0], mat[i][j])))
        # print(' ')
        if len(mat[i][j]) > 0:
            if mat[i][j] != 's':
                for f in mat[i][j]:
                    f_cnt = 0
                    
                    while f_cnt < len(mat[i][j]):
                        if f[0] > 0 and f[1] == s:
                            mat = fish_move(mat,i,j,f[0],s)
                            del mat[i][j][f_cnt]
                            f_cnt += 1
                        else:
                            f_cnt += 1

# 상어 움직여야함
                        
pprint(mat)
# a = [[[1, 2],[1, 3]],[[3,4],[4,5]]]
# print(a[0])
# print(list(map(lambda x: x[0], a[1])))
