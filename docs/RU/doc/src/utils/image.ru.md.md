# Модуль `image.py`

## Обзор

Модуль `image.py` предоставляет утилиты для работы с изображениями, включая асинхронную загрузку, сохранение, чтение и поиск случайных изображений. Он предназначен для использования в проектах, где требуется обработка изображений, таких как загрузка изображений по URL, сохранение их в локальное хранилище, а также рекурсивный поиск случайных изображений в указанной директории.

## Оглавление

- [Обзор](#обзор)
- [Основные функции](#основные-функции)
  - [`save_png_from_url`](#1-save_png_from_urlimage_url-str-filename-str--path---str--none)
  - [`save_png`](#2-save_pngimage_data-bytes-file_name-str--path---str--none)
  - [`get_image_data`](#3-get_image_datafile_name-str--path---bytes--none)
  - [`random_image`](#4-random_imageroot_path-str--path---str--none)
- [Установка и использование](#установка-и-использование)
- [Примеры использования](#примеры-использования)
  - [Загрузка изображения по URL и сохранение](#загрузка-изображения-по-url-и-сохранение)
  - [Сохранение изображения из данных](#сохранение-изображения-из-данных)
  - [Чтение данных изображения](#чтение-данных-изображения)
  - [Поиск случайного изображения](#поиск-случайного-изображения)
- [Логирование](#логирование)
- [Лицензия](#лицензия)
- [Автор](#автор)

## Основные функции

### 1. `save_png_from_url(image_url: str, filename: str | Path) -> str | None`

Асинхронно загружает изображение по указанному URL и сохраняет его локально в формате PNG.

**Параметры:**
- `image_url` (str): URL изображения для загрузки.
- `filename` (str | Path): Имя файла или путь, куда сохранить изображение.

**Возвращает:**
- `str | None`: Путь к сохранённому файлу или `None`, если операция завершилась неудачно.

**Пример:**

```python
import asyncio

asyncio.run(save_png_from_url("https://example.com/image.png", "local_image.png"))
```

---

### 2. `save_png(image_data: bytes, file_name: str | Path) -> str | None`

Асинхронно сохраняет переданные данные изображения в формате PNG.

**Параметры:**
- `image_data` (bytes): Двоичные данные изображения.
- `file_name` (str | Path): Имя файла или путь, куда сохранить изображение.

**Возвращает:**
- `str | None`: Путь к сохранённому файлу или `None`, если операция завершилась неудачно.

**Пример:**

```python
import asyncio

with open("example_image.png", "rb") as f:
    image_data = f.read()

asyncio.run(save_png(image_data, "saved_image.png"))
```

---

### 3. `get_image_data(file_name: str | Path) -> bytes | None`

Синхронно считывает двоичные данные изображения из указанного файла.

**Параметры:**
- `file_name` (str | Path): Имя файла или путь к изображению.

**Возвращает:**
- `bytes | None`: Двоичные данные изображения или `None`, если файл не найден или произошла ошибка.

**Пример:**

```python
data = get_image_data("saved_image.png")
print(data)  # Вывод: b'\x89PNG\r\n...'
```

---

### 4. `random_image(root_path: str | Path) -> str | None`

Рекурсивно ищет случайное изображение в указанной директории и возвращает путь к нему.

**Параметры:**
- `root_path` (str | Path): Директория для поиска изображений.

**Возвращает:**
- `str | None`: Путь к случайному изображению или `None`, если изображений не найдено.

**Пример:**

```python
random_image_path = random_image("path/to/images")
if random_image_path:
    print(f"Случайное изображение: {random_image_path}")
else:
    print("Изображений не найдено.")
```

---

## Установка и использование

1. Убедитесь, что у вас установлен Python 3.8 или выше.
2. Установите необходимые зависимости:

   ```bash
   pip install aiohttp aiofiles pillow
   ```

3. Импортируйте функции из модуля `image.py` в ваш проект:

   ```python
   from src.utils.image import save_png_from_url, save_png, get_image_data, random_image
   ```

---

## Примеры использования

### Загрузка изображения по URL и сохранение

```python
import asyncio

asyncio.run(save_png_from_url("https://example.com/image.png", "local_image.png"))
```

### Сохранение изображения из данных

```python
import asyncio

with open("example_image.png", "rb") as f:
    image_data = f.read()

asyncio.run(save_png(image_data, "saved_image.png"))
```

### Чтение данных изображения

```python
data = get_image_data("saved_image.png")
print(data)
```

### Поиск случайного изображения

```python
random_image_path = random_image("path/to/images")
if random_image_path:
    print(f"Случайное изображение: {random_image_path}")
else:
    print("Изображений не найдено.")
```

---

## Логирование

Модуль использует встроенный логгер для отслеживания ошибок и предупреждений. Убедитесь, что логгер настроен в вашем проекте для получения сообщений.

---

## Лицензия

Этот проект лицензирован под [MIT License](../LICENSE).

---

## Автор

hypo69