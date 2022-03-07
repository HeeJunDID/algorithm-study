from curses import pair_content
import sys
sys.stdin = open('./ex7.txt')
target = int(sys.stdin.readline())
broken_num = int(sys.stdin.readline())
button_list = list(sys.stdin.readline().split())
present = 100
plus_target = target
minus_target = target
cnt = 0
while True:
    if target == present:
        break
    
    plus_target += 1
    minus_target -= 1
    p_state, m_state, t_state= False, False, False
    
    p_list = list(str(plus_target))
    m_list = list(str(minus_target))
    t_list = list(str(target))
    for b in button_list:
        if b in p_list:
            p_state = True
        if b in m_list:
            m_state = True
        if b in t_list:
            t_state = True
    if p_state == False or m_state == False or t_state == False:
        if not t_state:
            cnt += len(t_list)
        elif not p_state:

            p_num = int(''.join(p_list))
            cnt += p_num - target
            cnt += len(p_list)
        elif not m_state:

            m_num = int(''.join(m_list))
            cnt += target - m_num
            cnt += len(m_list)
        break

print(cnt)

# 인터넷에서 찾은 답

import sys
input = sys.stdin.readline
target = int(input())
n = int(input())
broken = list(map(int, input().split()))

# 현재 채널에서 + 혹은 -만 사용하여 이동하는 경우
min_count = abs(100 - target)

for nums in range(1000001):
    nums = str(nums)
    
    for j in range(len(nums)):
        # 각 숫자가 고장났는지 확인 후, 고장 났으면 break
        if int(nums[j]) in broken:
            break

        # 고장난 숫자 없이 마지막 자리까지 왔다면 min_count 비교 후 업데이트
        elif j == len(nums) - 1:
            min_count = min(min_count, abs(int(nums) - target) + len(nums))

print(min_count)