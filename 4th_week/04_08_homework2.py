current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

def move_back(d, cur, room_map):
    if d == 0 and room_map[cur[0] + 1][cur[1]] != 1: # N
        cur[0] += 1
        return True
    if d == 1 and room_map[cur[0]][cur[1] - 1] != 1: # E
        cur[1] -= 1
        return True
    if d == 2 and room_map[cur[0] - 1][cur[1]] != 1: # S
        cur[0] -= 1
        return True
    if d == 3 and room_map[cur[0]][cur[1] + 1] != 1: # W
        cur[1] += 1
        return True
    return False

def rotate(d):
    if d == 0: #N -> W
        return 3
    else:
        return d - 1

def move_forward(d, cur, room_map):
    if d == 0 and room_map[cur[0] - 1][cur[1]] == 0: # N
        cur[0] -= 1
        return True
    if d == 1 and room_map[cur[0]][cur[1] + 1] == 0: # E
        cur[1] += 1
        return True
    if d == 2 and room_map[cur[0] + 1][cur[1]] == 0: # S
        cur[0] += 1
        return True
    if d == 3 and room_map[cur[0]][cur[1] - 1] == 0: # W
        cur[1] -= 1
        return True
    return False



def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    cur = [r, c]
    cleaned = 0
    while True:
        # 1. 청소 시작
        if room_map[cur[0]][cur[1]] == 0:
            cleaned += 1
            room_map[cur[0]][cur[1]] += 2

        # 청소되지 않은 빈칸이 없는 경우
        if room_map[cur[0] + 1][cur[1]] > 0 and room_map[cur[0] - 1][cur[1]] > 0 and \
            room_map[cur[0]][cur[1] + 1] > 0 and room_map[cur[0]][cur[1] - 1] > 0:

            # 후진이 가능한지
            if move_back(d, cur, room_map):
                continue
            else:
                return cleaned

        # 청소되지 않은 빈칸이 있는경우
        d = rotate(d)
        while not move_forward(d, cur, room_map):
            d = rotate(d)
        else:
            continue

# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))
current_room_map2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
print("정답 = 29 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(6,3,1,current_room_map2))
current_room_map3 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
print("정답 = 33 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(7,4,1,current_room_map3))
current_room_map4 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
print("정답 = 25 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(6,2,0,current_room_map4))