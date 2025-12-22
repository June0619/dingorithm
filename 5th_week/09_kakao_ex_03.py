
lines = [
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]

def solution(p_lines):
    for log in p_lines:
        log = LogInspector(log)

class LogInspector:

    def __init__(self, log_string):
        log_split = log_string.split(' ')
        end_time_arr = list(map(int, log_split[1][:8].split(':')))
        end_time_arr.append(int(log_split[1][9:]))

        end_time = end_time_arr[0] * 60 * 60 * 1000 + end_time_arr[1] * 60 * 1000 + end_time_arr[2] * 1000 + end_time_arr[3]

        duration_str = log_split[2]
        duration_str = duration_str.replace('s', '')

        duration_arr = list(map(int, duration_str.split('.')))
        duration = duration_arr[0] * 1000
        if len(duration_arr) > 1:
            duration += duration_arr[1]

        start_time = end_time - duration + 1

        print(end_time, start_time, duration)

solution(lines)