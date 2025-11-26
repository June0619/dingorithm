array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]

def merge(array1, array2):

    idx_a = 0
    idx_b = 0

    return_array = []

    la = len(array1)
    lb = len(array2)

    while idx_a < la and idx_b < lb:
        if array1[idx_a] >= array2[idx_b]:
            return_array.append(array2[idx_b])
            idx_b += 1
        else:
            return_array.append(array1[idx_a])
            idx_a += 1

    return_array.extend(array1[idx_a:])
    return_array.extend(array2[idx_b:])

    return return_array

print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge([-7, -1, 9, 40], [5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge([-1,2,3,5,40], [10,78,100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge([-1,-1,0], [1, 6, 9, 10]))