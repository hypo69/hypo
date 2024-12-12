# Модуль `image.py`

## Оглавление

1.  [Обзор](#обзор)
2.  [Функции](#функции)
    *   [`save_png_from_url`](#save_png_from_url)
    *   [`save_png`](#save_png)
    *   [`get_image_data`](#get_image_data)
    *   [`random_image`](#random_image)
3.  [Установка и использование](#установка-и-использование)
4.  [Примеры использования](#примеры-использования)
5.  [Логирование](#логирование)
6.  [Лицензия](#лицензия)
7.  [Автор](#автор)

## Обзор

Модуль `image.py` предоставляет утилиты для работы с изображениями, включая асинхронную загрузку, сохранение, чтение и поиск случайных изображений. Он предназначен для использования в проектах, где требуется обработка изображений, таких как загрузка изображений по URL, сохранение их в локальное хранилище, а также рекурсивный поиск случайных изображений в указанной директории.

## Функции

### `save_png_from_url`

**Описание**: Асинхронно загружает изображение по указанному URL и сохраняет его локально в формате PNG.

**Параметры**:
- `image_url` (str): URL изображения для загрузки.
- `filename` (str | Path): Имя файла или путь, куда сохранить изображение.

**Возвращает**:
- `str | None`: Путь к сохранённому файлу или `None`, если операция завершилась неудачно.

**Пример**:

```python
import asyncio

asyncio.run(save_png_from_url("https://example.com/image.png", "local_image.png"))
```

---

### `save_png`

**Описание**: Асинхронно сохраняет переданные данные изображения в формате PNG.

**Параметры**:
- `image_data` (bytes): Двоичные данные изображения.
- `file_name` (str | Path): Имя файла или путь, куда сохранить изображение.

**Возвращает**:
- `str | None`: Путь к сохранённому файлу или `None`, если операция завершилась неудачно.

**Пример**:

```python
import asyncio

with open("example_image.png", "rb") as f:
    image_data = f.read()

asyncio.run(save_png(image_data, "saved_image.png"))
```

---

### `get_image_data`

**Описание**: Синхронно считывает двоичные данные изображения из указанного файла.

**Параметры**:
- `file_name` (str | Path): Имя файла или путь к изображению.

**Возвращает**:
- `bytes | None`: Двоичные данные изображения или `None`, если файл не найден или произошла ошибка.

**Пример**:

```python
data = get_image_data("saved_image.png")
print(data)  # Вывод: b'\x89PNG\r\n...'
```

---

### `random_image`

**Описание**: Рекурсивно ищет случайное изображение в указанной директории и возвращает путь к нему.

**Параметры**:
- `root_path` (str | Path): Директория для поиска изображений.

**Возвращает**:
- `str | None`: Путь к случайному изображению или `None`, если изображений не найдено.

**Пример**:

```python
random_image_path = random_image("path/to/images")
if random_image_path:
    print(f"Случайное изображение: {random_image_path}")
else:
    print("Изображений не найдено.")
```

---

## Установка и использование

1.  Убедитесь, что у вас установлен Python 3.8 или выше.
2.  Установите необходимые зависимости:
    ```bash
    pip install aiohttp aiofiles pillow
    ```
3.  Импортируйте функции из модуля `image.py` в ваш проект:
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