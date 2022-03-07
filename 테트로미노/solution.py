import sys
from pprint import pprint
sys.stdin = open('./ex1.txt')
n, m = map(int,sys.stdin.readline().split())
n_map = []
for _ in range(n):
    n_map.append(list(sys.stdin.readline().split()))
v_map = [[False for _ in range(m)] for _ in range(n)]