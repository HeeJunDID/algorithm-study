# import sys
# sys.stdin = open('ex1.txt')
# ary = list(map(int,sys.stdin.readline().split()))
# # while True:
# #     cnt = 1
# temp = [ary[0]]
# dif = 0
# p_dif = ary[1] - ary[0]
# for i in range(1, len(ary)):
#     cnt = 0
#     while cnt 
#     for j in  range(cnt,cnt+)
# # for i in range(1,len(ary)):
# #     dif = ary[i] - ary[i-1]
# #     if p_dif == dif:
# #         temp.append(ary[i])
# # print(temp)
n, m = 5,5
data = [1,2,3,2,5]
result = 0
summary = 0
end = 0
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while summary < m and end < n:
        summary += data[end]
        end += 1
    # 부분 합이 m일 때 카운트 증가
    if summary == m:
        result += 1
    summary -= data[start]
print(result)