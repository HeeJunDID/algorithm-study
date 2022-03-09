import sys
sys.stdin = open('./ex2.txt')
n = int(sys.stdin.readline())
ans = 0
cnt = 1

while True:
    if n-(9*(10**(cnt-1))) > 0:
        ans += (9*(10**(cnt-1))) * cnt
        n = n-(9*(10**(cnt-1)))
    else:
        ans += cnt * n
        break
    cnt += 1
print(ans)
