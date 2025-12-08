seat_count = 9
vip_seat_array = [4, 7]

memo = {
    1: 1,
    2: 2
}

def fibo(n):
    if n in memo:
        return memo[n]
    result = fibo(n - 1) + fibo(n - 2)
    memo[n] = result
    return result

def get_all_ways_of_theater_seat(total_count, fixed_seat_array):

    seat_arr = list(range(1, total_count + 1))

    seat_split = []
    temp = []
    for i in seat_arr:
        if i not in fixed_seat_array:
            temp.append(i)
        else:
            seat_split.append(temp)
            temp = []
    else:
        seat_split.append(temp)

    result = 1
    for arr in seat_split:
        result *= fibo(len(arr))

    return result


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))

print("정답 = 4 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(9,[2,4,7]))
print("정답 = 26 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(11,[2,5]))
print("정답 = 6 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(10,[2,6,9]))