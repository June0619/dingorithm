input = [4, 6, 2, 9, 1]

def insertion_sort(array):

    sorted_array = []
    while array:
        n = array.pop(0)

        for i in range(len(sorted_array) - 1, -1, -1):
            if sorted_array[i] < n:
                sorted_array.insert(i+1, n)
                break
        else:
            sorted_array.insert(0, n)

    return sorted_array

# print(insertion_sort([4, 6, 2, 9, 1])) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ",insertion_sort([5,8,4,7,7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",insertion_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",insertion_sort([100,56,-3,32,44]))