start_range, end_range = map(int, input().split(' '))

prime_arr = [0] * end_range

def print_(result):
  if start_range <= result:
    print(result)

for idx in range(end_range):
  num = idx + 1
  if num == 1:
    continue
  if num == 2:
    for j in range(3, end_range, 2):
      prime_arr[j] += 1
    print_(num)
    continue
  if prime_arr[idx] == 0:
    for k in range(idx+num, end_range, num):
      prime_arr[k] += 1
    print_(num)
    continue
