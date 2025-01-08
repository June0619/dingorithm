def find_max_occurred_alphabet(string):

  arr = [0] * 26

  for i in range(len(string)):
    char = string[i]
    if str.isalpha(char):
      # arr[ord(char) - 97] += 1
      char_idx = ord(char) - ord('a')
      arr[char_idx] += 1

  max_occur_idx = arr.index(max(arr))
  return chr(max_occur_idx + ord('a'))

result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))