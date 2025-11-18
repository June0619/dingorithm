finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, array):
    array.sort()
    idx = (len(array) - 1) // 2
    if not array:
        return False

    if array[idx] == target:
        return True

    if array[idx] > target:
        return is_exist_target_number_binary(target, array[:idx])
    else:
        return is_exist_target_number_binary(target, array[idx+1:])

result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)