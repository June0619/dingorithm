n = int(input())

temp = set()
result = 0

for _ in range(n):
    input_str = input()
    if input_str == 'ENTER':
        result += len(temp)
        temp = set()
    else:
        temp.add(input_str)
else:
    result += len(temp)

print(result)
