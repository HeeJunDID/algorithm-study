import sys
from pprint import pprint
import copy
from itertools import combinations
from collections import Counter
sys.stdin = open("./ex3.txt")

n,m = map(int,sys.stdin.readline().strip().split())
lab = []
for i in range(n):
    lab.append(list(map(int,sys.stdin.readline().strip().split())))
def virus(lab, a, b):
    """
    바이러스가 퍼질수 있는 최대 위치
    lab = 연구소의 지도
    x = x좌표
    y = y좌표
    """
    dx = [0,0,1,-1] #하 상 우 좌
    dy = [1,-1,0,0]
    stack = [(a,b)]
    n, m = len(lab), len(lab[0])
    while stack:
        x, y = stack.pop()
        
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >=0 and nx<n and ny <m and lab[nx][ny] == 0:
                lab[nx][ny] = 2
                stack.append((nx,ny))
    return lab
def set_wall(lab):
    """
    벽을 세울 수 있는 모든 경우의 수의 맵을 뽑아냄
    """
    n,m = len(lab), len(lab[0])
    z_loc = []
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                z_loc.append((i,j))
    num_of_case = list(combinations(z_loc, 3))

    lab_of_case = []
    for c in num_of_case:
    
        temp_lab = copy.deepcopy(lab)
        x1, y1 = c[0]
        x2, y2 = c[1]
        x3, y3 = c[2]
        temp_lab[x1][y1] = 1
        temp_lab[x2][y2] = 1
        temp_lab[x3][y3] = 1
        lab_of_case.append(temp_lab)
    return lab_of_case

if __name__ == "__main__":
    answer_list = []
    for i in set_wall(lab):
        for q in range(n):
            for r in range(m):
                if i[q][r] == 2:
                    i = virus(i,q,r)
        answer_list.append(Counter(sum(i,[]))[0])
    print(max(answer_list))