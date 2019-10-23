import datetime


def get_albums_by_genre(albums, genre):
    """
    Get albums by genre

    :param list albums: albums' data
    :param str genre: genre to filter by

    :returns: all albums of given genre
    :rtype: list
    """
    albums_in_genre = []
    for album in albums:
        album_genre = album[3]
        if genre == album_genre:
            albums_in_genre.append(album)
    if albums_in_genre: 
        return albums_in_genre


def get_longest_album(albums):
    """
    Get album with biggest value in length field.
    If there are more than one such album return the first (by original lists' order)

    :param list albums: albums' data
    :returns: longest album
    :rtype: list
    """
    longest_album = max(albums, key=lambda x:x[-1])
    return longest_album


def get_total_albums_length(albums):
    """
    Get sum of lengths of all albums in minutes, rounded to 2 decimal places
    Example: 3:51 + 5:20 = 9.18
    :param list albums: albums' data
    :returns: total albums' length in minutes
    :rtype: float
    """
    albums_min = 0
    albums_sec = 0
    for album in albums:
        album_time = str(album[-1]).split(':')
        album_time = [int(x) for x in album_time]  # convert str to int for calculation
        
        album_min = album_time[0]
        album_sec = album_time[1]
        
        albums_min += album_min
        albums_sec += album_sec
    total_albums_time_in_sec = (albums_min*60) + album_sec
    return str(datetime.timedelta(seconds=total_albums_time_in_sec))


def get_genre_stats():
    pass


def get_last_oldest():
    pass


def get_last_oldest_of_genre():
    pass
