def find_genre_s(name):
    count = 0
    for a in name_genres:
        if a == name:
            count += 1
            return count  # после цикла
    print(count)
