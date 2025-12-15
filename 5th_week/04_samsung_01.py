from collections import deque

k = 4  # 말의 개수

chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
start_horse_location_and_directions = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]

n = len(chess_map)


def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    # render map
    stack_map = [[] for _ in range(n)]

    horse_graph = {}

    for i in range(n):
        for j in range(n):
            if game_map[i][j] < 2:
                stack_map[i].append([])
            else:
                stack_map[i].append(None)

    for i in range(len(horse_location_and_directions)):
        horse_status = horse_location_and_directions[i]
        horse_graph[i] = horse_status
        r = horse_status[0]
        c = horse_status[1]

        stack_map[r][c].append(i)


    repeated_count = 1

    while repeated_count <= 1000:
        temp = []
        for i in range(horse_count):
            temp.append(move(game_map, stack_map, i, horse_graph))

            if check_end_game(stack_map):
                return repeated_count

        if not True in temp:
            return -1

        repeated_count += 1
    return -1

def check_end_game(stack_map):
    for raw in stack_map:
        for col in raw:
            if len(col) == 4:
                return True
    else:
        return False

def move(game_map, stack_map, idx, horse_graph):
    r = horse_graph[idx][0]
    c = horse_graph[idx][1]

    retry_cnt = 2
    while retry_cnt > 0:
        d = horse_graph[idx][2]
        if d == 0:
            # 동쪽 확인
            if c + 1 == len(game_map) or game_map[r][c+1] == 2:
                horse_graph[idx][2] = 1
                retry_cnt -= 1
                continue
            # 빨간 칸
            if game_map[r][c+1] == 1:
                temp = []
                while True:
                    pop = stack_map[r][c].pop()
                    temp.append(pop)
                    horse_graph[pop][1] += 1
                    if pop == idx:
                        break
                stack_map[r][c + 1].extend(temp)
            # 흰 칸
            if game_map[r][c+1] == 0:
                temp = []
                while True:
                    pop = stack_map[r][c].pop()
                    temp.append(pop)
                    horse_graph[pop][1] += 1
                    if pop == idx:
                        break
                while temp:
                    stack_map[r][c + 1].append(temp.pop())
        if d == 1:
            # 서쪽 확인
            if c - 1 == -1 or game_map[r][c-1] == 2:
                horse_graph[idx][2] = 0
                retry_cnt -= 1
                continue
            # 빨간 칸
            if game_map[r][c - 1] == 1:
                temp = []
                while True:
                    pop = stack_map[r][c].pop()
                    temp.append(pop)
                    horse_graph[pop][1] -= 1
                    if pop == idx:
                        break
                stack_map[r][c - 1].extend(temp)
            # 흰 칸
            if game_map[r][c - 1] == 0:
                temp = []
                while True:
                    pop = stack_map[r][c].pop()
                    temp.append(pop)
                    horse_graph[pop][1] -= 1
                    if pop == idx:
                        break
                while temp:
                    stack_map[r][c - 1].append(temp.pop())
        if d == 2:
            # 북쪽 확인
            if r - 1 == -1 or game_map[r-1][c] == 2:
                horse_graph[idx][2] = 3
                retry_cnt -= 1
                continue
            # 빨간 칸
            if game_map[r - 1][c] == 1:
                temp = []
                while True:
                    pop = stack_map[r][c].pop()
                    temp.append(pop)
                    horse_graph[pop][0] -= 1
                    if pop == idx:
                        break
                stack_map[r - 1][c].extend(temp)
            # 흰 칸
            if game_map[r - 1][c] == 0:
                temp = []
                while True:
                    pop = stack_map[r][c].pop()
                    temp.append(pop)
                    horse_graph[pop][0] -= 1
                    if pop == idx:
                        break
                while temp:
                    stack_map[r - 1][c].append(temp.pop())
        if d == 3:
            # 남쪽 확인
            if r + 1 == len(game_map) or game_map[r+1][c] == 2:
                horse_graph[idx][2] = 2
                retry_cnt -= 1
                continue
            # 빨간 칸
            if game_map[r + 1][c] == 1:
                temp = []
                while True:
                    pop = stack_map[r][c].pop()
                    temp.append(pop)
                    horse_graph[pop][0] += 1
                    if pop == idx:
                        break
                stack_map[r + 1][c].extend(temp)
            # 흰 칸
            if game_map[r + 1][c] == 0:
                temp = []
                while True:
                    pop = stack_map[r][c].pop()
                    temp.append(pop)
                    horse_graph[pop][0] += 1
                    if pop == idx:
                        break
                while temp:
                    stack_map[r + 1][c].append(temp.pop())
        return True
    else:
        return False

print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다

start_horse_location_and_directions = [
    [0, 1, 0],
    [1, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
print("정답 = 9 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))

start_horse_location_and_directions = [
    [0, 1, 0],
    [0, 1, 1],
    [0, 1, 0],
    [2, 1, 2]
]
print("정답 = 3 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))