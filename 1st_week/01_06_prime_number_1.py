def find_prime_list_under_number(number):
  prime_arr = []
  for i in range(number):
    if i > 1 and is_prime(i):
      prime_arr.append(i)
  return prime_arr

def is_prime(number):
  for i in range(2, number // 2):
    if number % i == 0:
      return False

  return True

result = find_prime_list_under_number(20)
print(result)