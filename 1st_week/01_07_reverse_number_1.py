input_str = "11001100110011000001"

def find_count_to_turn_out_to_all_zero_or_all_one(string):

    start_char = string[0]
    is_relay = False
    cnt = 0

    for idx in range(1, len(string)):
      if string[idx] != start_char and not is_relay:
        is_relay = True
        cnt += 1

      if string[idx] == start_char:
        is_relay = False


    return cnt


result = find_count_to_turn_out_to_all_zero_or_all_one(input_str)
print(result)