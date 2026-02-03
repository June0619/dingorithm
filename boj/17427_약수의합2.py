input_number = int(input())

result = 0
for i in range(1, input_number + 1):
    count = input_number // i
    result += count * i

print(result)