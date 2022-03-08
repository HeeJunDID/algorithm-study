import sys
sys.stdin = open('./ex1.txt')

def check_year(m,n,x,y):
    x -= 1
    y -= 1
    state = False
    k = x
    while k < n*m:
        if k % n == y:
            return k+1
            break
        k += m
    else:
        return -1

t = int(sys.stdin.readline())
for _ in range(t):
    m, n, x, y = list(map(int, sys.stdin.readline().split()))
    print(check_year(m,n,x,y))