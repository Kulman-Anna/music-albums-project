# -*- coding: utf-8 -*-
"""
Файл: data_manager.py
Модуль для загрузки и сохранения данных об исполнителях, альбомах и треках из CSV.
"""

import csv
import os

def load_artists(data_dir):
    path = os.path.join(data_dir, "artists.csv")
    if not os.path.exists(path):
        return []
    artists = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            artists.append({
                "artist_id": int(row["artist_id"]),
                "artist_name": row["artist_name"]
            })
    return artists

def load_albums(data_dir):
    path = os.path.join(data_dir, "albums.csv")
    if not os.path.exists(path):
        return []
    albums = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            albums.append({
                "album_id": int(row["album_id"]),
                "artist_id": int(row["artist_id"]),
                "album_title": row["album_title"],
                "release_year": int(row["release_year"]),
                "genre": row["genre"]
            })
    return albums

def load_tracks(data_dir):
    path = os.path.join(data_dir, "tracks.csv")
    if not os.path.exists(path):
        return []
    tracks = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tracks.append({
                "track_id": int(row["track_id"]),
                "album_id": int(row["album_id"]),
                "track_number": int(row["track_number"]),
                "track_title": row["track_title"],
                "track_duration": row["track_duration"]
            })
    return tracks

def save_albums(data_dir, albums):
    path = os.path.join(data_dir, "albums.csv")
    fieldnames = ["album_id", "artist_id", "album_title", "release_year", "genre"]
    with open(path, "w", encoding="utf-8", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for album in albums:
            writer.writerow(album)