# -*- coding: utf-8 -*-
import pytest
from albums import add_album, find_albums_by_artist, remove_album, update_album

@pytest.fixture
def sample_artists():
    return [
        {"artist_id": 1, "artist_name": "The Beatles"},
        {"artist_id": 2, "artist_name": "Pink Floyd"}
    ]

@pytest.fixture
def sample_albums():
    return [
        {"album_id": 1, "artist_id": 1, "album_title": "Abbey Road", "release_year": 1969, "genre": "Rock"},
        {"album_id": 2, "artist_id": 2, "album_title": "The Dark Side of the Moon", "release_year": 1973, "genre": "Progressive Rock"}
    ]

def test_add_album(sample_artists, sample_albums):
    updated = add_album(sample_artists, sample_albums, "Pink Floyd", "Meddle", 1971, "Rock")
    assert len(updated) == 3
    assert updated[-1]["album_title"] == "Meddle"
    with pytest.raises(ValueError):
        add_album(sample_artists, sample_albums, "Nonexistent", "Test", 2000, "Pop")

def test_find_albums_by_artist(sample_artists, sample_albums):
    result = find_albums_by_artist(sample_artists, sample_albums, "The Beatles")
    assert len(result) == 1
    assert result[0]["album_title"] == "Abbey Road"
    result = find_albums_by_artist(sample_artists, sample_albums, "Nonexistent")
    assert len(result) == 0

def test_remove_album(sample_albums):
    updated = remove_album(sample_albums, 1)
    assert len(updated) == 1
    with pytest.raises(ValueError):
        remove_album(updated, 999)

def test_update_album(sample_albums):
    updated = update_album(sample_albums, 2, title="Meddle", year=1971)
    album = [a for a in updated if a["album_id"] == 2][0]
    assert album["album_title"] == "Meddle"
    assert album["release_year"] == 1971
    with pytest.raises(ValueError):
        update_album(updated, 999, title="Unknown")