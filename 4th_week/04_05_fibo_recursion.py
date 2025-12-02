input = 10

def fibo_recursion(n):
    if n > 2:
        return n
    return fibo_recursion(n - 1) + fibo_recursion(n - 2)

print(fibo_recursion(input))  # 6765