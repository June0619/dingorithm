#https://www.acmicpc.net/problem/13549
from collections import deque
N, K = map(int, input().split())

def solution(n, k):

    # 탐색 -> bfs
    next_location = deque([])
    # 이론상 최대 시간이 100_000이므로
    visited = [100_001 for _ in range(100_001)]

    next_location.append((n, 0))

    visited[n] = 0

    while next_location:
        location, time = next_location.popleft()

        if location == k:
            return time

        # 맵 처음인 경우
        if location >= 1 and time + 1 < visited[location - 1]:
            next_location.append((location - 1, time + 1))
            visited[location - 1] = time + 1

        # 맵 끝까지 간 경우
        if location < 100_000 and time + 1 < visited[location + 1]:
            next_location.append((location + 1, time + 1))
            visited[location + 1] = time + 1

        # 순간이동
        if 2 * location <= 100_000 and time < visited[2 * location]:
            next_location.appendleft((location * 2, time))
            visited[location * 2] = time

    return -1

print(solution(N, K))
