import sys
from pprint import pprint
sys.stdin = open('./ex3.txt')

n = int(sys.stdin.readline())
board = []
for _ in range(n):
    board.append(list(sys.stdin.readline().replace('\n','')))

def check(board):
    n = len(board)
    ans = 1
    for i in range(len(board)):
        cnt = 1
        for j in range(1,len(board)):
            if board[i][j] == board[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt:
                ans = cnt
        cnt = 1
        for j in range(1, len(board)):
            if board[j][i] == board[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt:
                ans = cnt
    return ans



if __name__ == "__main__":
    for i in board:
        print(i)
    max_ans = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if j+1 < n:
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
                if max_ans < check(board):
                    max_ans = check(board)
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
                
            if i+1 < n:
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                if max_ans < check(board):
                    max_ans = check(board)
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
    print(max_ans)