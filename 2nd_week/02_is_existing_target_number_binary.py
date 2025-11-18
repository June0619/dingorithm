finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    idx = (len(array) -1) // 2

    if not array:
        return False

    if array[idx] == target:
        return True

    if array[idx] > target:
        return is_existing_target_number_binary(target, array[:idx])
    else:
        return is_existing_target_number_binary(target, array[idx:])

result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)