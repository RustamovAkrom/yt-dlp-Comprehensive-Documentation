# yt-dlp: Полная Документация

**`yt-dlp`** — это форк `youtube-dl`, который предоставляет дополнительные функции и улучшения. Библиотека позволяет загружать видео и аудио с YouTube и других платформ, а также извлекать метаданные.

## Установка

Чтобы установить `yt-dlp`, используйте pip:

```bash
pip install yt-dlp
```

## Основные функции

- **Загрузка видео и аудио**: Поддержка загрузки с различных платформ.
- **Извлечение метаданных**: Получение информации о видео, таких как заголовок, описание, теги и т.д.
- **Форматирование**: Конвертация видео в различные форматы.
- **Работа с плейлистами**: Загрузка видео из плейлистов.

## Основное использование

### Загрузка видео

Для загрузки видео используйте следующий код:

```python
import yt_dlp as youtube_dl

ydl_opts = {
    'format': 'best',  # Выбор лучшего доступного качества
    'outtmpl': 'path/to/save/%(title)s.%(ext)s',  # Шаблон имени файла
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=VIDEO_ID'])
```

### Извлечение метаданных

Для получения метаданных видео используйте код:

```python
import yt_dlp as youtube_dl

ydl_opts = {
    'quiet': True,  # Без вывода логов
    'skip_download': True,  # Не загружать видео
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info('https://www.youtube.com/watch?v=VIDEO_ID', download=False)
    print(info_dict)
```

### Загрузка аудио

Для загрузки только аудио:

```python
import yt_dlp as youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',  # Выбор лучшего доступного аудио
    'extractaudio': True,  # Извлечение аудио
    'outtmpl': 'path/to/save/%(title)s.%(ext)s',  # Шаблон имени файла
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=VIDEO_ID'])
```

### Загрузка плейлиста

Для загрузки всех видео из плейлиста:

```python
import yt_dlp as youtube_dl

ydl_opts = {
    'format': 'best',
    'outtmpl': 'path/to/save/%(playlist)s/%(title)s.%(ext)s',  # Шаблон имени файла с подкаталогом для плейлиста
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/playlist?list=PLAYLIST_ID'])
```

## Дополнительные параметры

- **`format`**: Определяет качество и формат видео. Можно использовать `'best'`, `'worst'`, `'bestaudio/best'`, и другие.
- **`outtmpl`**: Шаблон для имен файлов и директорий, куда будет сохраняться контент.
- **`quiet`**: Устанавливает режим без вывода логов.
- **`skip_download`**: Пропускает загрузку видео, оставляя только извлечение информации.

## Документация и ресурсы

- **[Официальный репозиторий yt-dlp](https://github.com/yt-dlp/yt-dlp)**: Основной ресурс для получения кода и документации.
- **[Техническая документация](https://github.com/yt-dlp/yt-dlp/blob/master/README.md)**: Полный список опций и параметров.
- **[Сообщество и поддержка](https://github.com/yt-dlp/yt-dlp/issues)**: Место для общения с другими пользователями и получения помощи.

## Заключение

`yt-dlp` — это мощный инструмент для загрузки и извлечения контента с YouTube и других платформ. Он предоставляет гибкость и множество возможностей для работы с видео и аудио. Используйте его для автоматизации задач и интеграции с вашими проектами.
