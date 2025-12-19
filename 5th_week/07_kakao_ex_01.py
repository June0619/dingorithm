from collections import deque

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def map_print(p_board):
    for line in p_board:
        print(line)

def solution(p_board, p_moves):
    board_size = len(p_board)
    bucket = []

    dq = deque(p_moves)

    while dq:
        move_index = dq.popleft() - 1
        # 0이 아닐때까지 집게 내리기
        for i in range(board_size):
            if p_board[i][move_index] != 0:
                #만나면 뽑기
                bucket.append(p_board[i][move_index])
                p_board[i][move_index] = 0
                break

    break_count = 0
    prv_char = None

    while True:
        for i in range(len(bucket)):
            if prv_char == bucket[i]:
                break_count += 2
                bucket.pop(i)
                bucket.pop(i-1)
                prv_char = None
                break
            else:
                prv_char = bucket[i]
        else:
            break

    return break_count

print(solution(board, moves))