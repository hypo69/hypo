# Модуль `image.py`

## Обзор

Модуль `image.py` предоставляет асинхронные функции для загрузки, сохранения и получения данных изображений.

## Оглавление
1. [Функции](#функции)
    - [`save_png_from_url`](#save_png_from_url)
    - [`save_png`](#save_png)
    - [`get_image_data`](#get_image_data)
    - [`random_image`](#random_image)

## Функции

### `save_png_from_url`

**Описание**: Загружает изображение по URL-адресу и асинхронно сохраняет его локально.

**Параметры**:
- `image_url` (str): URL-адрес для загрузки изображения.
- `filename` (str | Path): Имя файла для сохранения изображения.

**Возвращает**:
- `str | None`: Путь к сохраненному файлу или `None`, если операция не удалась.

**Пример:**
```python
>>> asyncio.run(save_png_from_url("https://example.com/image.png", "local_image.png"))
'local_image.png'
```

### `save_png`

**Описание**: Асинхронно сохраняет изображение в формате PNG.

**Параметры**:
- `image_data` (bytes): Бинарные данные изображения.
- `file_name` (str | Path): Имя файла для сохранения изображения.

**Возвращает**:
- `str | None`: Путь к сохраненному файлу или `None`, если операция не удалась.

**Пример:**
```python
>>> with open("example_image.png", "rb") as f:
...     image_data = f.read()
>>> asyncio.run(save_png(image_data, "saved_image.png"))
'saved_image.png'
```

### `get_image_data`

**Описание**: Извлекает бинарные данные файла, если он существует.

**Параметры**:
- `file_name` (str | Path): Имя файла для чтения.

**Возвращает**:
- `bytes | None`: Бинарные данные файла, если он существует, или `None`, если файл не найден или произошла ошибка.

**Пример:**
```python
>>> get_image_data("saved_image.png")
b'\x89PNG\r\n...'
```

### `random_image`

**Описание**: Рекурсивно ищет случайное изображение в указанном каталоге и возвращает его путь.

**Параметры**:
- `root_path` (str | Path): Каталог для поиска изображений.

**Возвращает**:
- `str | None`: Путь к случайному изображению или `None`, если изображения не найдены.

**Пример:**
```python
>>> random_image("path/to/images")
'path/to/images/subfolder/random_image.png'
```