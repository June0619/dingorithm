import time


# repeat = int(input())

def solution(p_number):

    # 1, 2, 3 배열 초기화
    visited = set()
    # 숫자 초기화
    n1, n2, n3 = p_number, 0, 0
    stack = [(n1, n2, n3)]
    visited.add((n1, n2, n3))

    while stack:
        n1, n2, n3 = stack.pop()

        # 3 하나 나오는 경우
        if n1 >= 3 and (n1 - 3, n2, n3 + 1) not in visited:
            visited.add((n1 - 3, n2, n3 + 1))
            stack.append((n1 - 3, n2, n3 + 1))
        # 2 하나 나오는 경우
        if n1 >= 2 and (n1 - 2, n2 + 1, n3) not in visited:
            visited.add((n1 - 2, n2 + 1, n3))
            stack.append((n1 - 2, n2 + 1, n3))

    return len(visited)

# for _ in range(repeat):
#     solution(int(input()))
start_time = time.time() # 시작 시간 기록
for n in [10000]:
    print(solution(n))
end_time = time.time() # 종료 시간 기록

# 소수점 5자리까지 출력 (초 단위)
print(f"실행 시간: {end_time - start_time:.5f} sec")