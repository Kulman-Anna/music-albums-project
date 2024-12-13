# -*- coding: utf-8 -*-
import argparse
import os
from data_manager import load_artists, load_albums, load_tracks, save_albums
from albums import add_album, find_albums_by_artist, remove_album, update_album

def main():
    parser = argparse.ArgumentParser(description="Music Albums Management CLI")
    parser.add_argument("--data_dir", required=True, help="Путь к директории данных")
    parser.add_argument("--action", required=False,
                        choices=["list_artists", "list_albums", "add_album", "find_albums", "remove_album", "update_album"],
                        default="list_albums")
    parser.add_argument("--artist", help="Исполнитель")
    parser.add_argument("--title", help="Название альбома")
    parser.add_argument("--year", type=int, help="Год выпуска")
    parser.add_argument("--genre", help="Жанр")
    parser.add_argument("--album_id", type=int, help="ID альбома")

    args = parser.parse_args()

    artists = load_artists(args.data_dir)
    albums = load_albums(args.data_dir)
    tracks = load_tracks(args.data_dir)

    if args.action == "list_artists":
        for artist in artists:
            print(f"{artist['artist_id']}. {artist['artist_name']}")
    elif args.action == "list_albums":
        for album in albums:
            artist_name = next((a["artist_name"] for a in artists if a["artist_id"] == album["artist_id"]), "Unknown")
            print(f"{album['album_id']}. {artist_name} - {album['album_title']} ({album['release_year']}, {album['genre']})")
    elif args.action == "add_album":
        if not args.artist or not args.title or not args.year or not args.genre:
            print("Недостаточно данных для добавления альбома.")
        else:
            try:
                albums = add_album(artists, albums, args.artist, args.title, args.year, args.genre)
                save_albums(args.data_dir, albums)
                print("Альбом успешно добавлен.")
            except ValueError as e:
                print(e)
    elif args.action == "find_albums":
        if not args.artist:
            print("Укажите --artist для поиска.")
        else:
            found = find_albums_by_artist(artists, albums, args.artist)
            if found:
                for album in found:
                    artist_name = next((a["artist_name"] for a in artists if a["artist_id"] == album["artist_id"]), "Unknown")
                    print(f"{album['album_id']}. {artist_name} - {album['album_title']}")
            else:
                print("Ничего не найдено.")
    elif args.action == "remove_album":
        if not args.album_id:
            print("Укажите --album_id для удаления.")
        else:
            try:
                albums = remove_album(albums, args.album_id)
                save_albums(args.data_dir, albums)
                print("Альбом успешно удален.")
            except ValueError as e:
                print(e)
    elif args.action == "update_album":
        if not args.album_id:
            print("Укажите --album_id для обновления.")
        else:
            try:
                albums = update_album(albums, args.album_id, title=args.title, year=args.year, genre=args.genre)
                save_albums(args.data_dir, albums)
                print("Альбом успешно обновлен.")
            except ValueError as e:
                print(e)

if __name__ == "__main__":
    main()