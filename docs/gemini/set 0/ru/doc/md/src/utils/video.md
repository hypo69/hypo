# Модуль hypotez/src/utils/video.py

## Обзор

Модуль `video.py` предоставляет асинхронные функции для загрузки и сохранения видеофайлов, а также для извлечения данных из них.  Включает обработку ошибок и логирование для надежной работы.

## Функции

### `save_video_from_url`

**Описание**: Асинхронно загружает видео с указанного URL и сохраняет его локально. Обрабатывает сетевые ошибки и ошибки сохранения файла.

**Параметры**:

- `url` (str): URL видео, которое нужно загрузить.
- `save_path` (str): Путь для сохранения загруженного видео.

**Возвращает**:

- `Optional[Path]`: Путь к сохраненному файлу или `None`, если операция завершилась неудачно. Возвращает `None` при ошибках и если файл имеет размер 0 байт.

**Вызывает исключения**:

- `aiohttp.ClientError`: При сетевых проблемах во время загрузки.


### `get_video_data`

**Описание**: Извлекает бинарные данные из видеофайла, если он существует. Обрабатывает ошибки открытия и чтения файла.

**Параметры**:

- `file_name` (str): Путь к видеофайлу.

**Возвращает**:

- `Optional[bytes]`: Бинарные данные файла, если он существует, или `None`, если файл не найден или произошла ошибка.


## Примеры

```python
import asyncio
# ... (Пример использования save_video_from_url)

# ... (Пример использования get_video_data)
```

## Дополнительные сведения

- Для корректной работы модуля требуется установка библиотек `aiohttp`, `aiofiles` и `pathlib`.


## Логирование

Модуль использует `src.logger` для записи сообщений об ошибках и успешных операциях.  В случае возникновения ошибки, подробная информация о ней выводится в журнал.

## Использование

Для использования функций модуля импортируйте их:

```python
from hypotez.src.utils.video import save_video_from_url, get_video_data
```

Затем вы можете вызвать функции, как показано в примерах.  Не забудьте обрабатывать возможные возвращаемые значения `None`.
```
```
```python
import asyncio
from hypotez.src.utils.video import save_video_from_url

async def main():
  url = "https://example.com/video.mp4" #Замените на действительный URL!
  save_path = "local_video.mp4"
  result = await save_video_from_url(url, save_path)
  if result:
    print(f"Видео сохранено по пути: {result}")
  else:
    print("Сохранение видео не удалось.")

if __name__ == "__main__":
  asyncio.run(main())