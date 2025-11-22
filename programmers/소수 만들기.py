def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True

def bfs(nums, arr):
    arr.append(nums[0])

    if len(arr) == 3:
        return 1 if is_prime(sum(arr)) else 0
    else:
        remain_length = len(nums) - (3 - len(arr))
        answer_count = 0
        for i in range(1, remain_length + 1):
            answer_count += bfs(nums[i:], arr.copy())
        return answer_count

def solution(nums):
    summary = 0
    for i in range(len(nums) - 2):
        summary += bfs(nums[i:], [])
    return summary