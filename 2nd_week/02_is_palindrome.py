input_string = "abccba"

def is_palindrome(string):

    target_idx = len(string) // 2

    str_arr = list(string)
    for i in range(target_idx):
        reverse_idx = -(i+1)
        if str_arr[i] != str_arr[reverse_idx]:
            return False

    return True

print(is_palindrome(input_string))