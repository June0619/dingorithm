def find_max_num(array):
    max_value = -999

    # for i in range(len(array)):
    #   if max_value < array[i]:
    #     max_value = array[i]

    for num in array:
      if num > max_value:
        max_value = num

    return max_value

print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))