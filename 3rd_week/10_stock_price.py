prices = [1, 2, 3, 2, 3]

def get_price_not_fall_periods(prices):

    answer = [0] * len(prices)

    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                answer[i] = j - i
                break
        else:
            answer[i] = len(prices) - i - 1

    return answer

print(get_price_not_fall_periods(prices))

print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods(prices))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ",
      get_price_not_fall_periods([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ",
      get_price_not_fall_periods([1, 5, 3, 6, 7, 6, 5]))