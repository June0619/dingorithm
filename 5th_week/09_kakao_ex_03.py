class LogInspector:
    def __init__(self, log_string):
        log_split = log_string.split(' ')

        # parse endtime
        end_time_arr = list(map(int, log_split[1][:8].split(':')))
        end_time_arr.append(int(log_split[1][9:]))

        end_time = end_time_arr[0] * 60 * 60 * 1000 # hour
        end_time += end_time_arr[1] * 60 * 1000 # minute
        end_time += end_time_arr[2] * 1000 # second
        end_time += end_time_arr[3] # milli

        # parse duration
        duration_str = log_split[2]
        duration_str = duration_str.replace('s', '')
        duration_arr = list(map(int, duration_str.split('.')))
        duration = duration_arr[0] * 1000

        # 2s 와 같은 예외케이스 처리
        if len(duration_arr) > 1:
            duration += duration_arr[1]

        # 시작시간 계산
        start_time = end_time - duration + 1

        self.start_time = start_time
        self.end_time = end_time
        self.duration = duration

    def is_range(self, lange_start, lange_end):
        return (self.end_time >= lange_start >= self.start_time) or (
                self.start_time <= lange_end <= self.end_time) or (
            self.start_time >= lange_start and self.end_time <= lange_end
        )

def solution(p_lines):
    log_array = []
    for log in p_lines:
        log_array.append(LogInspector(log))

    # 가장 빠른 시작시간
    log_array.sort(key=lambda x: x.end_time)

    result = 0

    for i in range(len(log_array)):
        log = log_array[i]
        # 가장 최신꺼부터 1000 millis 씩 끊어서 범위를 조회

        lange_start, lange_end  = log.end_time, log.end_time + 999

        lange_count = 0

        for j in range(i+1, len(log_array)):
            log_2 = log_array[j]

            if log_2.is_range(lange_start, lange_end):
                lange_count += 1

        #본인 포함
        lange_count += 1

        result = max(result, lange_count)

    return result


lines = [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]

print(solution(lines))