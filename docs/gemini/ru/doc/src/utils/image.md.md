# Модуль `image`

## Обзор

Модуль `image.py` предоставляет утилиты для работы с изображениями, включая асинхронную загрузку, сохранение, чтение и поиск случайных изображений. Он предназначен для использования в проектах, требующих обработки изображений, таких как загрузка изображений из URL-адресов, их сохранение в локальное хранилище и рекурсивный поиск случайных изображений в указанном каталоге.

## Оглавление

1. [Функции](#Функции)
    - [`save_png_from_url`](#save_png_from_url)
    - [`save_png`](#save_png)
    - [`get_image_data`](#get_image_data)
    - [`random_image`](#random_image)
2. [Установка и использование](#Установка-и-использование)
3. [Примеры использования](#Примеры-использования)
4. [Логирование](#Логирование)
5. [Лицензия](#Лицензия)
6. [Автор](#Автор)

## Функции

### `save_png_from_url`

**Описание**:
Асинхронно загружает изображение из указанного URL и сохраняет его локально в формате PNG.

**Параметры**:
- `image_url` (str): URL-адрес изображения для загрузки.
- `filename` (str | Path): Имя файла или путь, куда будет сохранено изображение.

**Возвращает**:
- `str | None`: Путь к сохраненному файлу или `None`, если операция не удалась.

**Пример:**
```python
import asyncio

asyncio.run(save_png_from_url("https://example.com/image.png", "local_image.png"))
```

---

### `save_png`

**Описание**:
Асинхронно сохраняет предоставленные данные изображения в формате PNG.

**Параметры**:
- `image_data` (bytes): Бинарные данные изображения.
- `file_name` (str | Path): Имя файла или путь, куда будет сохранено изображение.

**Возвращает**:
- `str | None`: Путь к сохраненному файлу или `None`, если операция не удалась.

**Пример:**
```python
import asyncio

with open("example_image.png", "rb") as f:
    image_data = f.read()

asyncio.run(save_png(image_data, "saved_image.png"))
```

---

### `get_image_data`

**Описание**:
Синхронно считывает бинарные данные изображения из указанного файла.

**Параметры**:
- `file_name` (str | Path): Имя файла или путь к изображению.

**Возвращает**:
- `bytes | None`: Бинарные данные изображения или `None`, если файл не найден или произошла ошибка.

**Пример:**
```python
data = get_image_data("saved_image.png")
print(data)  # Output: b'\x89PNG\r\n...'
```

---

### `random_image`

**Описание**:
Рекурсивно ищет случайное изображение в указанном каталоге и возвращает его путь.

**Параметры**:
- `root_path` (str | Path): Каталог для поиска изображений.

**Возвращает**:
- `str | None`: Путь к случайному изображению или `None`, если изображения не найдены.

**Пример:**
```python
random_image_path = random_image("path/to/images")
if random_image_path:
    print(f"Random image: {random_image_path}")
else:
    print("No images found.")
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

### Загрузка изображения из URL и его сохранение

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
    print(f"Random image: {random_image_path}")
else:
    print("No images found.")
```

---

## Логирование

Модуль использует встроенный логгер для отслеживания ошибок и предупреждений. Убедитесь, что логгер настроен в вашем проекте для получения сообщений.

---

## Лицензия

Этот проект лицензирован в соответствии с [MIT License](../LICENSE).

---

## Автор

hypo69