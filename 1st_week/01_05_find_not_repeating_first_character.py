def find_not_repeating_first_character(string):
  not_repeating_char = []

  for i in range(len(string)):
    if not not_repeating_char.__contains__(string[i]):
      not_repeating_char.append(string[i])
    else:
      not_repeating_char.pop(not_repeating_char.index(string[i]))

  if len(not_repeating_char) == 0:
    not_repeating_char.append('_')

  return not_repeating_char[0]


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))
