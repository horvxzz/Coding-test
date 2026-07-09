def solution(board, k):
    a=0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i+j<=k:
                a+=board[i][j]
    return a