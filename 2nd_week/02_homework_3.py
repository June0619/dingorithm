numbers = [1, 1, 1, 1, 1]
target_number = 3

def dfs_sum(array, summary):
    summary += array.pop(0)
    if len(array) >= 1:
        count = 0
        array2 = array.copy()
        count += dfs_sum(array, summary)
        array2[0] = -array2[0]
        count += dfs_sum(array2, summary)
        return count
    else:
        if summary == target_number:
            return 1
        else:
            return 0

def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    array2 = array.copy()
    array2[0] = -array2[0]
    return dfs_sum(array, 0) + dfs_sum(array2, 0)

print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!