from collections import deque

map1 = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]

n, m = 5, 5

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

def render_map(graph):
    temp = [['#' for _ in range(m)] for _ in range(n)]
    b_loc = None
    r_loc = None
    o_loc = None
    for key in graph.keys():
        if key == 'B':
            b_loc = graph[key]
        if key == 'R':
            r_loc = graph[key]
        if key == 'O':
            o_loc = graph[key]

        temp[key[0]][key[1]] = '.'

    temp[b_loc[0]][b_loc[1]] = 'B'
    temp[r_loc[0]][r_loc[1]] = 'R'
    temp[o_loc[0]][o_loc[1]] = 'O'

def to_east(adjusted_graph):
    # 오른쪽 기울이기
    blue_i, blue_j = adjusted_graph['B']
    red_i, red_j = adjusted_graph['R']
    goal_i, goal_j = adjusted_graph['O']

    # 오른쪽 벽에서 가까운거 먼저
    if blue_j > red_j:
        # move B first
        while adjusted_graph[(blue_i, blue_j)][0]:
            blue_j += 1
            adjusted_graph['B'][1] += 1
            # loose check

            if goal_i == blue_i and goal_j == blue_j:
                return False

        # move R
        while adjusted_graph[(red_i, red_j)][0] and not (red_j + 1 == blue_j and red_i == blue_i):
            red_j += 1
            adjusted_graph['R'][1] += 1

            if goal_i == red_i and goal_j == red_j:
                return True
    else:
        # move R first
        while adjusted_graph[(red_i, red_j)][0]:
            red_j += 1
            adjusted_graph['R'][1] += 1

            if goal_i == red_i and goal_j == red_j:
                return True
        # move B
        while adjusted_graph[(blue_i, blue_j)][0] and not (red_j == blue_j + 1 and red_i == blue_i):
            blue_j += 1
            adjusted_graph['B'][1] += 1
            # loose check

            if goal_i == blue_i and goal_j == blue_j:
                return False

def to_west(adjusted_graph):
    # 왼쪽 기울이기
    blue_i, blue_j = adjusted_graph['B']
    red_i, red_j = adjusted_graph['R']
    goal_i, goal_j = adjusted_graph['O']

    # 왼쪽 벽에서 가까운거 먼저
    if blue_j < red_j:
        # move B first
        while adjusted_graph[(blue_i, blue_j)][1]:
            blue_j -= 1
            adjusted_graph['B'][1] -= 1
            # loose check

            if goal_i == blue_i and goal_j == blue_j:
                return False

        # move R
        while adjusted_graph[(red_i, red_j)][1] and not (red_j - 1 == blue_j and red_i == blue_i):
            red_j -= 1
            adjusted_graph['R'][1] -= 1

            if goal_i == red_i and goal_j == red_j:
                return True
    else:
        # move R first
        while adjusted_graph[(red_i, red_j)][1]:
            red_j -= 1
            adjusted_graph['R'][1] -= 1

            if goal_i == red_i and goal_j == red_j:
                return True
        # move B
        while adjusted_graph[(blue_i, blue_j)][1] and not (red_j == blue_j - 1 and red_i == blue_i):
            blue_j -= 1
            adjusted_graph['B'][1] -= 1
            # loose check

            if goal_i == blue_i and goal_j == blue_j:
                return False

def to_north(adjusted_graph):
    # 북쪽 기울이기
    blue_i, blue_j = adjusted_graph['B']
    red_i, red_j = adjusted_graph['R']
    goal_i, goal_j = adjusted_graph['O']

    # 북쪽 벽에서 가까운거 (작은거) 먼저
    if blue_i < red_i:
        # move B first
        while adjusted_graph[(blue_i, blue_j)][3]:
            blue_i -= 1
            adjusted_graph['B'][0] -= 1
            # loose check

            if goal_i == blue_i and goal_j == blue_j:
                return False

        # move R
        while adjusted_graph[(red_i, red_j)][3] and not (red_i - 1 == blue_i and red_j == blue_j):
            red_i -= 1
            adjusted_graph['R'][0] -= 1

            if goal_i == red_i and goal_j == red_j:
                return True
    else:
        # move R first
        while adjusted_graph[(red_i, red_j)][3]:
            red_i -= 1
            adjusted_graph['R'][0] -= 1

            if goal_i == red_i and goal_j == red_j:
                return True
        # move B
        while adjusted_graph[(blue_i, blue_j)][3] and not (red_i == blue_i - 1 and red_j == blue_j):
            blue_i -= 1
            adjusted_graph['B'][3] -= 1
            # loose check

            if goal_i == blue_i and goal_j == blue_j:
                return False

def to_south(adjusted_graph):
    # 남쪽 기울이기
    blue_i, blue_j = adjusted_graph['B']
    red_i, red_j = adjusted_graph['R']
    goal_i, goal_j = adjusted_graph['O']

    # 남쪽 벽에서 가까운거 (큰거) 먼저
    if blue_i > red_i:
        # move B first
        while adjusted_graph[(blue_i, blue_j)][2]:
            blue_i += 1
            adjusted_graph['B'][0] += 1
            # loose check

            if goal_i == blue_i and goal_j == blue_j:
                return False

        # move R
        while adjusted_graph[(red_i, red_j)][2] and not (red_i + 1 == blue_i and red_j == blue_j):
            red_i += 1
            adjusted_graph['R'][0] += 1

            if goal_i == red_i and goal_j == red_j:
                return True
    else:
        # move R first
        while adjusted_graph[(red_i, red_j)][2]:
            red_i += 1
            adjusted_graph['R'][0] += 1

            if goal_i == red_i and goal_j == red_j:
                return True
        # move B
        while adjusted_graph[(blue_i, blue_j)][2] and not (red_i == blue_i + 1 and red_j == blue_j):
            blue_i += 1
            adjusted_graph['B'][0] += 1
            # loose check

            if goal_i == blue_i and goal_j == blue_j:
                return False


def is_available_to_take_out_only_red_marble(game_map):

    adjusted_graph = render_path(game_map)
    # 0 1 2 3 -> e w s n



    #move e
    print(to_south(adjusted_graph))

    print(adjusted_graph)


    return False


print(is_available_to_take_out_only_red_marble(map1))  # True 를 반환해야 합니다
