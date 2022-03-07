import sys
import numpy as np
sys.stdin = open('./ex4.txt')

e, s, m = map(int, sys.stdin.readline().split())
print(e,s,m)
a, b, c = 1, 1, 1
print(a, b, c)
cnt = 1
while True:
    if a == e and b == s and c == m:
        print(cnt)
        break
    a += 1
    b += 1
    c += 1
    if a > 15:
        a = 1
    if b > 28:
        b = 1
    if c > 19:
        c = 1
    cnt += 1
    