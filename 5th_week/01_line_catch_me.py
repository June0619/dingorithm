from collections import deque

def get_cur_ac(time):
    result = 0
    for n in range(1, time + 1):
        result += n
    return result

def catch_me(cony_loc, brown_loc):

    location_queue = deque()
    location_queue.append((brown_loc, 0))
    while True:
        cur_status = location_queue.popleft()
        cur_brown_loc = cur_status[0]
        cur_time = cur_status[1]
        cur_ac = get_cur_ac(cur_time)
        cur_cony_loc = cony_loc + cur_ac

        if cur_brown_loc == cur_cony_loc:
            return cur_time
        if cur_cony_loc > 200_000:
            return cur_time

        cur_time += 1

        move_back_loc = cur_brown_loc - 1
        move_forward_loc = cur_brown_loc + 1
        move_twice_loc = cur_brown_loc * 2

        if move_back_loc >= 0 and (move_back_loc, cur_time) not in location_queue:
            location_queue.append((move_back_loc, cur_time))

        if move_forward_loc <= 200_000 and (move_forward_loc, cur_time) not in location_queue:
            location_queue.append((move_forward_loc, cur_time))

        if move_twice_loc <= 200_000 and (move_twice_loc, cur_time) not in location_queue:
            location_queue.append((move_twice_loc, cur_time))

print(catch_me(11, 2))  # 5가 나와야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))