memo = {
    0: (1, 0),
    1: (0, 1)
}

def fibo(n):
    if n in memo:
        return memo[n]
    else:
        n_1 = fibo(n-1)
        n_2 = fibo(n-2)

        memo[n] = (n_1[0] + n_2[0], n_1[1] + n_2[1])
        return memo[n]

repeat = int(input())

for _ in range(repeat):
    result = fibo(int(input()))
    print(result[0], result[1])


