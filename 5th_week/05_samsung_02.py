from collections import deque

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]

def render_path(game_map):
    adjusted_graph = {}

    for i in range(1, len(game_map)):
        for j in range(1, len(game_map[i])):

            if game_map[i][j] == 'B':
                adjusted_graph['B'] = [i, j]

            if game_map[i][j] == 'R':
                adjusted_graph['R'] = [i, j]

            if game_map[i][j] == 'O':
                adjusted_graph['O'] = [i, j]

            if game_map[i][j] != '#':
                adjusted_graph[(i, j)] = []
                # 동쪽
                if game_map[i][j + 1] != '#':
                    adjusted_graph[(i, j)].append(True)
                else:
                    adjusted_graph[(i, j)].append(False)
                # 서쪽
                if game_map[i][j - 1] != '#':
                    adjusted_graph[(i, j)].append(True)
                else:
                    adjusted_graph[(i, j)].append(False)
                # 남쪽
                if game_map[i + 1][j] != '#':
                    adjusted_graph[(i, j)].append(True)
                else:
                    adjusted_graph[(i, j)].append(False)
                # 북쪽
                if game_map[i - 1][j] != '#':
                    adjusted_graph[(i, j)].append(True)
                else:
                    adjusted_graph[(i, j)].append(False)
    return adjusted_graph

def is_available_to_take_out_only_red_marble(game_map):

    adjusted_graph = render_path(game_map)
    # 0 1 2 3 -> e w s n

    #move e
    blue_i, blue_j = adjusted_graph['B']
    red_i, red_j = adjusted_graph['R']

    print(blue_i, blue_j)

    goal_i, goal_j = adjusted_graph['O']

    # move B
    while adjusted_graph[(blue_i, blue_j)][0]:
        blue_j += 1
        adjusted_graph['B'][1] += 1
        # loose check

        if goal_i == blue_i and goal_j == blue_j:
            return False

    while adjusted_graph[(red_i, red_j)][0]:
        red_j += 1
        adjusted_graph['R'][1] += 1

        if goal_i == red_i and goal_j == red_j:
            return True

    print(adjusted_graph)

    return False


print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다


#
# game_map = [
#     ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
#     ["#", ".", "O", ".", ".", ".", ".", "R", "B", "#"],
#     ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
# ]
# print("정답 = False / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))
#
#
# game_map = [
# ["#", "#", "#", "#", "#", "#", "#"],
# ["#", ".", ".", "R", "#", "B", "#"],
# ["#", ".", "#", "#", "#", "#", "#"],
# ["#", ".", ".", ".", ".", ".", "#"],
# ["#", "#", "#", "#", "#", ".", "#"],
# ["#", "O", ".", ".", ".", ".", "#"],
# ["#", "#", "#", "#", "#", "#", "#"]
# ]
# print("정답 = True / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))