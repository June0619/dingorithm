import itertools
import sys

n, m = map(int, input().split(' '))
city_map = [list(map(int, input().split())) for _ in range(n)]

# n, m = 5, 1
# city_map = [
#     [1, 2, 0, 0, 0],
#     [1, 2, 0, 0, 0],
#     [1, 2, 0, 0, 0],
#     [1, 2, 0, 0, 0],
#     [1, 2, 0, 0, 0]
# ]

def solution(param_map):
    # 모든 집 위치 구하기
    house_loc = []
    chicken_loc = []

    for i in range(n):
        for j in range(n):
            if param_map[i][j] == 1:
                house_loc.append((i, j))
            if param_map[i][j] == 2:
                chicken_loc.append((i, j))

    combinations = list(itertools.combinations(chicken_loc, m))
    # print(combinations)

    min_value = sys.maxsize
    for com in combinations:
        city_chicken_score = 0
        # print(list(com))
        for h_loc in house_loc:
            temp = list(map(lambda x: get_chicken_distance(x, h_loc), com))
            city_chicken_score += min(temp)
        min_value = min(min_value, city_chicken_score)

    return min_value

def get_chicken_distance(loc_1, loc_2):
    x_1 = loc_1[0]
    x_2 = loc_2[0]
    y_1 = loc_1[1]
    y_2 = loc_2[1]
    x_distance = x_1 - x_2
    y_distance = y_1 - y_2
    if x_distance < 0:
        x_distance = -x_distance
    if y_distance < 0:
        y_distance = -y_distance
    return x_distance + y_distance

print(solution(city_map))