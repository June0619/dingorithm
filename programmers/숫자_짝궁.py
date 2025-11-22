# https://school.programmers.co.kr/learn/courses/30/lessons/131128
def solution(X, Y):

    array1 = list(X)
    array2 = list(Y)

    array1_count = [0] * 10
    array2_count = [0] * 10

    result_array = []

    for n in array1:
        array1_count[int(n)] += 1

    for n in array2:
        array2_count[int(n)] += 1

    for number in range(10):
        number_count = min(array1_count[number], array2_count[number])

        for _ in range(number_count):
            result_array.append(number)

    if len(result_array) == 0:
        return '-1'

    result_array.reverse()

    result_string = ''.join(map(str, result_array))

    return result_string if result_string[0] != '0' else '0'
