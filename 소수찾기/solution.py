import sys
sys.stdin = open("./ex1.txt")

n = int(sys.stdin.readline())
n_l = list(map(int,sys.stdin.readline().split()))
cnt = 0
for i in n_l:
    if i == 1:
        continue
    j = 2
    while j != i:
        if i%j == 0:
            break
        j += 1
        if i==j:
            cnt += 1
print(cnt)