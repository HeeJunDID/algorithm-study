import sys
from pprint import pprint
sys.stdin = open('./ex1.txt')
n = int(sys.stdin.readline())
target = int(sys.stdin.readline())

ary = [[0 for _ in range(n)] for _ in range(n)]
pprint(ary)
x, y = n//2, n//2
print(x,y)
ary[x][y] = 1
cnt = 1
dx = [0,1,-1,0]
dy = [1,0,0,-1]
x, y = x+dx[1], y+dy[1]
d = 0
while True:
    for i in range(8*cnt+1):
        nx = x+dx[d]
        ny = y+dy[d]
        
