def build_fibo():
    dp = [0] * (40 + 2)
    dp[0] = 1
    dp[1] = 2
    for i in range(2, 40 + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp

fibo = build_fibo()

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
        result *= fibo[len(arr)-1]

    return result

seat_count = int(input())
repeat_count = int(input())

seat_array = []
for _ in range(repeat_count):
    seat_array.append(int(input()))

print(get_all_ways_of_theater_seat(seat_count, seat_array))
