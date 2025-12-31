# https://www.acmicpc.net/problem/2178
from collections import deque
#입력시간 개선
import sys
input = sys.stdin.readline

input_n, input_m = map(int, input().split())

# 한번에 초기화
input_miro = [list(map(int, list(input().strip()))) for _ in range(input_n)]

def solution(n, m, miro):
    # 방문 체크 방향 벡터 사용
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    queue = deque([])
    queue.append((0, 0, 1))

    # visited 체크 2차원 set과 튜플 초기화 비용보다 2차원 배열이 약간 더 경제적
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True

    while queue:
        y, x, score = queue.popleft()

        if x == m - 1 and y == n - 1:
            return score

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < m and 0 <= ny < n:
                if miro[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((ny, nx, score + 1))
    return -1

print(solution(input_n, input_m, input_miro))