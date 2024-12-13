# Music Albums Management CLI

## Описание
Данная программа позволяет управлять коллекцией музыкальных альбомов, исполнителей и треков через консольный интерфейс.

Функционал:
- Загрузка данных из CSV-файлов (artists, albums, tracks)
- Добавление новых альбомов
- Поиск альбомов по исполнителю
- Удаление и обновление информации об альбомах

## Установка
```bash
git clone https://github.com/yourusername/music-albums-project.git
cd music-albums-project
pip install -r requirements.txt

## Команды для использования функций
1. Просмотр списка исполнителей: python main.py --data_dir ./data --action list_artists
2. Просмотр списка альбомов: python main.py --data_dir ./data --action list_albums
3. Добавление нового альбома: python main.py --data_dir ./data --action add_album --artist "The Beatles" --title "Let It Be" --year 1970 --genre "Rock"
4. Поиск альбомов по исполнителю: python main.py --data_dir ./data --action find_albums --artist "The Beatles"
5. Удаление альбома по ID: python main.py --data_dir ./data --action remove_album --album_id 1
6. Обновление информации об альбоме: python main.py --data_dir ./data --action update_album --album_id 2 --title "Meddle" --year 1971 --genre "Rock"

## Запуск тестов
python -m pytest