# https://www.acmicpc.net/problem/2178
from collections import deque

input_n, input_m = map(int, input().split())

input_miro = []

for _ in range(input_n):
    input_line = input()
    input_miro.append(list(map(int, list(input_line))))

def solution(n, m, miro):
    queue = deque([])
    queue.append((0, 0, 1))

    visited = set()
    visited.add((0, 0))

    while queue:
        location_tuple = queue.popleft()
        y = location_tuple[0]
        x = location_tuple[1]
        score = location_tuple[2]

        if x == m - 1 and y == n - 1:
            return score

        if x - 1 >= 0 and miro[y][x - 1] == 1 and (y, x - 1) not in visited:
            queue.append((y, x - 1, score + 1))
            visited.add((y, x - 1))
        if x + 1 < m and miro[y][x + 1] == 1 and (y, x + 1) not in visited:
            queue.append((y, x + 1, score + 1))
            visited.add((y, x + 1))
        if y - 1 >= 0 and miro[y - 1][x] == 1 and (y - 1, x) not in visited:
            queue.append((y - 1, x, score + 1))
            visited.add((y - 1, x))
        if y + 1 < n and miro[y + 1][x] == 1 and (y + 1, x) not in visited:
            queue.append((y + 1, x, score + 1))
            visited.add((y + 1, x))
    else:
        return None

print(solution(input_n, input_m, input_miro))