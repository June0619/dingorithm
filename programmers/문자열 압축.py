def solution(string):
    max_rate = len(string) // 2

    results = {}
    for i in range(1, max_rate + 1):
        arr = [string[j:j+i] for j in range(0, len(string), i)]

        temp = None
        compressed_cnt = 0
        continue_cnt= 0
        compressed_flag = False
        for c in arr:
            if temp == c:
                if not compressed_flag:
                    compressed_flag = True
                continue_cnt += 1
                compressed_cnt += len(c)
            else:
                if compressed_flag:
                    compressed_flag = False
                    compressed_cnt -= len(str(continue_cnt+1))
                    continue_cnt = 0

            temp = c
        else:
            if compressed_flag:
                compressed_cnt -= len(str(continue_cnt+1))
                continue_cnt = 0

        results[i] = compressed_cnt

    max_compressed = 0
    for i in results.values():
        max_compressed = max(max_compressed, i)

    return len(string) - max_compressed