def get_melon_best_album(genre_array, play_array):

    play_dict = {}
    rank_dict = {}

    for i in range(len(genre_array)):
        try:
            play_dict[genre_array[i]].append((i, play_array[i]))
            rank_dict[genre_array[i]] += play_array[i]
        except KeyError:
            play_dict[genre_array[i]] = [(i, play_array[i])]
            rank_dict[genre_array[i]] = play_array[i]

    sorted_rank_keys = sorted(rank_dict.keys(), key=lambda k: rank_dict[k], reverse=True)

    return_arr = []

    for key in sorted_rank_keys:
        arr = play_dict[key]
        return_arr.extend(sorted(arr, key=lambda t: t[1], reverse=True)[:2])

    return [x[0] for x in return_arr]

print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))