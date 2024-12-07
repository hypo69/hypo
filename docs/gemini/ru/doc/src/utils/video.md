# Модуль `hypotez/src/utils/video.py`

## Обзор

Модуль `video.py` предоставляет асинхронные функции для загрузки и сохранения видеофайлов из URL, а также для извлечения данных из сохранённых файлов. Он обрабатывает ошибки и использует логирование для надёжной работы.

## Функции

### `save_video_from_url`

**Описание**: Загружает видео из URL и сохраняет его локально асинхронно. Обрабатывает сетевые проблемы и ошибки сохранения файла.

**Параметры**:
- `url` (str): URL видео для загрузки.
- `save_path` (str): Путь для сохранения загруженного видео.

**Возвращает**:
- `Optional[Path]`: Путь к сохранённому файлу, или `None`, если операция завершилась неудачно (в случае ошибок, пустого файла или отсутствия файла).

**Вызывает исключения**:
- `aiohttp.ClientError`: Возникает при сетевых проблемах во время загрузки.


### `get_video_data`

**Описание**: Извлекает двоичные данные из видеофайла, если он существует. Обрабатывает ошибки открытия файла.

**Параметры**:
- `file_name` (str): Путь к видеофайлу для чтения.

**Возвращает**:
- `Optional[bytes]`: Двоичные данные файла, если он существует, или `None` при ошибке или отсутствии файла.

**Вызывает исключения**:
- `Exception`: Возникает при ошибках чтения файла.


## Примеры использования

```python
import asyncio
import pathlib

# Пример загрузки видео
async def download_example():
    url = "https://example.com/video.mp4"  # Замените на действительный URL!
    save_path = "local_video.mp4"
    result = await save_video_from_url(url, save_path)
    if result:
        print(f"Видео сохранено по пути: {result}")
    else:
        print("Ошибка при сохранении видео.")

# Пример извлечения данных
def read_example():
  file_path = pathlib.Path("local_video.mp4") # Путь к сохранённому видео
  data = get_video_data(str(file_path))
  if data:
      print("Первые 10 байтов:", data[:10])
  else:
      print("Ошибка при чтении файла.")
    

# Запуск примеров
asyncio.run(download_example())
read_example()
```

**Примечание**:  В примере `download_example` используется асинхронный вызов, поэтому для запуска необходим `asyncio.run()`. Пример `read_example` - синхронный. Не забудьте заменить `"https://example.com/video.mp4"` на действительный URL, иначе загрузка не будет работать.  Также убедитесь, что у вас установлен aiohttp и aiofiles.


```python
# Дополнительная информация (полезно при использовании):
# Подключение к логгеру, например, при необходимости:
# from src.logger import logger