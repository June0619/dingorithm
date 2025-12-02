input = 10

memo = {
    1: 1,
    2: 1
}

def fibo_dynamic(n):
    if n in memo:
        return memo[n]
    result = fibo_dynamic(n - 1) + fibo_dynamic(n - 2)
    memo[n] = result
    return result


print(fibo_dynamic(input))  # 6765