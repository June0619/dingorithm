#https://www.acmicpc.net/problem/13549
from collections import deque
N, K = map(int, input().split())

def solution(n, k):

    # 이론상 최대 시간이 100_000이므로
    MAX_SIZE = 100_001
    # 방문하지 않은 지점 -1 로 처리
    visited = [-1] * MAX_SIZE

    # 탐색 : 0-1 bfs
    # 해당 그래프는 가중치가 있는 그래프임
    queue = deque([n])
    visited[n] = 0

    while queue:
        location = queue.popleft()

        if location == k:
            return visited[location]

        # 1. 순간이동 하는 경우
        # 가중치가 가장 높으므로 (0) appendleft
        # 범위체크 및 방문체크
        if 0 <= location * 2 < MAX_SIZE and visited[location * 2] == -1:
            visited[location * 2] = visited[location]
            queue.appendleft(location * 2)

        # 2. 앞뒤로 걷는 경우
        # 가중치가 낮으므로 (1) append
        for next_location in (location - 1, location + 1):
            if 0 <= next_location < MAX_SIZE and visited[next_location] == -1:
                visited[next_location] = visited[location] + 1
                queue.append(next_location)

    return -1

print(solution(N, K))
