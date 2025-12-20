def solution(p_m, p_musicinfos):
    music_info_arr = list(map(lambda x: MusicInfo(x), p_musicinfos))

    min_tmep = 0
    answer = '(None)'
    for music in music_info_arr:
        if music.is_this_music(p_m) and music.played_minute > min_tmep:
            answer = music.name
            min_tmep = music.played_minute

    return answer

class MusicInfo:
    def __init__(self, music_info_str):
        music_info_array = music_info_str.split(',')

        start_time = music_info_array[0]
        end_time = music_info_array[1]
        end_hour = int(end_time.split(':')[0])
        end_minute = int(end_time.split(':')[1]) + end_hour * 60

        start_hour = int(start_time.split(':')[0])
        start_minute = int(start_time.split(':')[1]) + start_hour * 60

        self.melody = music_info_array[3]
        self.played_minute = end_minute - start_minute
        self.name = music_info_array[2]

        converted = self.__convert__(self.melody)

        self.full_melody = ''
        for i in range(self.played_minute):
            self.full_melody += converted[i % len(converted)]


    def is_this_music(self, p_music):
        converted_p_music = self.__convert__(p_music)
        return converted_p_music in self.full_melody

    def __str__(self):
        return self.name

    @staticmethod
    def __convert__(p_str):
        temp = p_str
        temp = temp.replace('C#', 'c')
        temp = temp.replace('D#', 'd')
        temp = temp.replace('F#', 'f')
        temp = temp.replace('G#', 'g')
        temp = temp.replace('A#', 'a')
        temp = temp.replace('B#', 'b')

        return temp