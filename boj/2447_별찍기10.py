import math

def convert_star(n):
    if n == 1:
        return '***\n* *\n***\n'
    else:
        arr = convert_star(n - 1).split('\n')
        arr2 = [s * 3 for s in arr]

        x = 3 ** (n-1)
        arr3 = arr2.copy()
        for i in range(len(arr3) - 1):
            st1 = arr3[i]
            arr3[i] = st1[:x] + ' ' * x + st1[2*x:]

        return '\n'.join(arr2) + '\n'.join(arr3) + '\n'.join(arr2)

n = int(input())

size = 0

while n != 1:
    n = n // 3
    size += 1

print(convert_star(size))








