from collections import deque

n, m = map(int, input().split(' '))

game_map = [list(input()) for _  in range(n)]

best_count = [999]

def min_custom(n1, n2):
    temp = 999
    if n1 > 0:
        temp = min(temp, n1)
    if n2 > 0:
        temp = min(temp, n2)

    if temp == 999:
        return -1
    else:
        return temp

def render_objects(param_map):
    graph = {}
    locations = {}

    # reachable place => True
    # unreachable place => False

    for i in range(1, n):
        for j in range(1, m):
            if param_map[i][j] != '#':
                graph[(i,j)] = [
                    # E, W, S, N
                    param_map[i][j+1] != '#',
                    param_map[i][j-1] != '#',
                    param_map[i+1][j] != '#',
                    param_map[i-1][j] != '#'
                ]

            if param_map[i][j] == 'B':
                locations['B'] = [i, j]
            elif param_map[i][j] == 'R':
                locations['R'] = [i, j]
            elif param_map[i][j] == 'O':
                locations['O'] = [i, j]

    return [graph, locations]

def render_map(graph, locations):
    # render wall
    rendered = [['#' for _ in range(m)] for _ in range(n)]

    for key in graph.keys():
        rendered[key[0]][key[1]] = '.'

    rendered[locations['B'][0]][locations['B'][1]] = 'B'
    rendered[locations['R'][0]][locations['R'][1]] = 'R'
    rendered[locations['O'][0]][locations['O'][1]] = 'O'

    return rendered

def move_to_east(param_map, try_count):
    if try_count > 10:
        return -1
    if best_count[0] < try_count:
        return -1

    objects = render_objects(param_map)
    graph = objects[0]
    locations = objects[1]

    init_b_loc = locations['B'][1]
    init_r_loc = locations['R'][1]

    # E -> 0
    while graph[tuple(locations['B'])][0]:
        locations['B'][1] += 1
        # Blue ball goal in
        if locations['B'] == locations['O']:
            is_blue_goal_in = True
            return -1

    # E -> 0
    while graph[(tuple(locations['R']))][0]:
        locations['R'][1] += 1
        # Red ball goal in
        if locations['R'] == locations['O']:
            is_red_goal_in = True
            best_count[0] = try_count
            return try_count

    # 충돌 처리 (아무 구멍에도 들어가지 않았을 경우)
    if (locations['B'][0] == locations['R'][0]
        and locations['B'][1] == locations['R'][1]):
        if init_b_loc > init_r_loc:
            locations['R'][1] -= 1
        else:
            locations['B'][1] -= 1

    rendered_map = render_map(graph=graph, locations=locations)
    return min_custom(move_to_north(rendered_map, try_count+1), move_to_south(rendered_map, try_count+1))

def move_to_west(param_map, try_count):
    if try_count > 10:
        return -1
    if best_count[0] < try_count:
        return -1

    objects = render_objects(param_map)
    graph = objects[0]
    locations = objects[1]

    init_b_loc = locations['B'][1]
    init_r_loc = locations['R'][1]

    # W -> 1
    while graph[tuple(locations['B'])][1]:
        locations['B'][1] -= 1
        # Blue ball goal in
        if locations['B'] == locations['O']:
            is_blue_goal_in = True
            return -1

    # W -> 1
    while graph[(tuple(locations['R']))][1]:
        locations['R'][1] -= 1
        # Red ball goal in
        if locations['R'] == locations['O']:
            is_red_goal_in = True
            best_count[0] = try_count
            return try_count

    # 충돌 처리 (아무 구멍에도 들어가지 않았을 경우)
    if (locations['B'][0] == locations['R'][0]
        and locations['B'][1] == locations['R'][1]):
        if init_b_loc < init_r_loc:
            locations['R'][1] += 1
        else:
            locations['B'][1] += 1

    rendered_map = render_map(graph=graph, locations=locations)
    return min_custom(move_to_north(rendered_map, try_count+1), move_to_south(rendered_map, try_count+1))

def move_to_south(param_map, try_count):
    if try_count > 10:
        return -1
    if best_count[0] < try_count:
        return -1

    objects = render_objects(param_map)
    graph = objects[0]
    locations = objects[1]

    init_b_loc = locations['B'][0]
    init_r_loc = locations['R'][0]

    # S -> 2
    while graph[tuple(locations['B'])][2]:
        locations['B'][0] += 1
        # Blue ball goal in
        if locations['B'] == locations['O']:
            is_blue_goal_in = True
            return -1

    # S -> 2
    while graph[(tuple(locations['R']))][2]:
        locations['R'][0] += 1
        # Red ball goal in
        if locations['R'] == locations['O']:
            is_red_goal_in = True
            best_count[0] = try_count
            return try_count

    # 충돌 처리 (아무 구멍에도 들어가지 않았을 경우)
    if (locations['B'][0] == locations['R'][0]
        and locations['B'][1] == locations['R'][1]):
        if init_b_loc > init_r_loc:
            locations['R'][0] -= 1
        else:
            locations['B'][0] -= 1

    rendered_map = render_map(graph=graph, locations=locations)
    return min_custom(move_to_east(rendered_map, try_count+1), move_to_west(rendered_map, try_count+1))

def move_to_north(param_map, try_count):
    if try_count > 10:
        return -1
    if best_count[0] < try_count:
        return -1

    objects = render_objects(param_map)
    graph = objects[0]
    locations = objects[1]

    init_b_loc = locations['B'][0]
    init_r_loc = locations['R'][0]

    # N -> 3
    while graph[tuple(locations['B'])][3]:
        locations['B'][0] -= 1
        # Blue ball goal in
        if locations['B'] == locations['O']:
            is_blue_goal_in = True
            return -1

    # S -> 2
    while graph[(tuple(locations['R']))][3]:
        locations['R'][0] -= 1
        # Red ball goal in
        if locations['R'] == locations['O']:
            is_red_goal_in = True
            best_count[0] = try_count
            return try_count

    # 충돌 처리 (아무 구멍에도 들어가지 않았을 경우)
    if (locations['B'][0] == locations['R'][0]
        and locations['B'][1] == locations['R'][1]):
        if init_b_loc < init_r_loc:
            locations['R'][0] += 1
        else:
            locations['B'][0] += 1

    rendered_map = render_map(graph=graph, locations=locations)

    return min_custom(move_to_east(rendered_map, try_count+1), move_to_west(rendered_map, try_count+1))

def solve(param_map):

    result = min_custom(
        min_custom(move_to_south(param_map, 1), move_to_north(param_map, 1)),
        min_custom(move_to_east(param_map, 1), move_to_west(param_map, 1))
    )

    return result

print(solve(game_map))  # True 를 반환해야 합니다