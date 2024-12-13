# -*- coding: utf-8 -*-
"""
Файл: albums.py
Модуль с функциями для управления музыкальными альбомами.
"""

def add_album(artists, albums, artist_name, title, year, genre):
    """
    Добавить новый альбом в коллекцию.

    Args:
        artists (list[dict]): Список исполнителей.
        albums (list[dict]): Список альбомов.
        artist_name (str): Имя исполнителя.
        title (str): Название альбома.
        year (int): Год выпуска.
        genre (str): Жанр.

    Returns:
        list[dict]: Обновленный список альбомов.

    Raises:
        ValueError: Если исполнитель не найден или такой альбом уже существует.
    """
    normalized = artist_name.strip().lower()
    matched_artists = [a for a in artists if a["artist_name"].lower() == normalized]
    if not matched_artists:
        raise ValueError(f"Artist '{artist_name}' not found.")
    artist_id = matched_artists[0]["artist_id"]

    # Проверка уникальности альбома для данного исполнителя (по названию)
    new_title = title.strip().lower()
    if any(a["artist_id"] == artist_id and a["album_title"].lower() == new_title for a in albums):
        raise ValueError(f"Album '{title}' by '{artist_name}' already exists.")

    new_id = max((a["album_id"] for a in albums), default=0) + 1
    new_album = {
        "album_id": new_id,
        "artist_id": artist_id,
        "album_title": title.strip(),
        "release_year": int(year),
        "genre": genre.strip()
    }
    albums.append(new_album)
    return albums


def find_albums_by_artist(artists, albums, artist_name):
    """
    Найти альбомы по имени исполнителя.

    Args:
        artists (list[dict]): Список исполнителей.
        albums (list[dict]): Список альбомов.
        artist_name (str): Имя исполнителя для поиска.

    Returns:
        list[dict]: Список альбомов, соответствующих исполнителю.
    """
    normalized = artist_name.strip().lower()
    matched_artists = [a for a in artists if a["artist_name"].lower() == normalized]
    if not matched_artists:
        return []
    artist_id = matched_artists[0]["artist_id"]
    return [a for a in albums if a["artist_id"] == artist_id]


def remove_album(albums, album_id):
    """
    Удалить альбом по его ID.

    Args:
        albums (list[dict]): Список альбомов.
        album_id (int): ID альбома для удаления.

    Returns:
        list[dict]: Обновленный список альбомов.

    Raises:
        ValueError: Если альбом не найден.
    """
    before = len(albums)
    albums = [a for a in albums if a["album_id"] != album_id]
    if len(albums) == before:
        raise ValueError(f"Cannot remove: album with ID {album_id} not found.")
    return albums


def update_album(albums, album_id, title=None, year=None, genre=None):
    """
    Обновить информацию об альбоме по его ID.

    Args:
        albums (list[dict]): Список альбомов.
        album_id (int): ID альбома для обновления.
        title (Optional[str]): Новое название альбома.
        year (Optional[int]): Новый год выпуска.
        genre (Optional[str]): Новый жанр.

    Returns:
        list[dict]: Обновленный список альбомов.

    Raises:
        ValueError: Если альбом не найден.
    """
    for album in albums:
        if album["album_id"] == album_id:
            if title is not None:
                album["album_title"] = title.strip()
            if year is not None:
                album["release_year"] = int(year)
            if genre is not None:
                album["genre"] = genre.strip()
            return albums
    raise ValueError(f"Album with ID {album_id} not found.")
