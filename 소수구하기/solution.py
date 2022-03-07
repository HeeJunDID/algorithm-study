import sys
sys.stdin = open('./ex1.txt')

n, m = map(int, sys.stdin.readline().split())
max_num = 1000000
check = [False for _ in range(max_num + 1)]
check[0] = check[1] = True
for i in range(2, max_num+1):
    if not check[i]:
        j = i + i
        while j <= max_num:
            check[j] = True
            j += i

for k in range(n,m+1):
    if check[k] == False:
        print(k)
