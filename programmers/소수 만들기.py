import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def dfs(nums, start, depth, current_sum):
    # 3개를 고른 경우
    if depth == 3:
        return 1 if is_prime(current_sum) else 0

    count = 0
    # 현재 위치부터 남은 숫자들 순회
    for i in range(start, len(nums)):
        count += dfs(nums, i + 1, depth + 1, current_sum + nums[i])
    return count

def solution(nums):
    return dfs(nums, 0, 0, 0)

print(solution([1,2,7,6,4]))