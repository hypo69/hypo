# Модуль для конвертации изображений из WebP в PNG

## Обзор

Модуль предназначен для конвертации изображений из формата WebP в формат PNG. Он содержит функцию `convert_images`, которая принимает на вход директорию с WebP-изображениями и директорию, куда следует сохранить сконвертированные PNG-изображения.

## Подробней

Этот модуль используется для преобразования изображений из формата WebP в формат PNG. WebP - современный формат изображений, разработанный Google, который обеспечивает лучшую компрессию по сравнению с JPEG. Однако, не все программы и устройства поддерживают WebP, поэтому может возникнуть необходимость конвертировать изображения в более распространенный формат, такой как PNG.
Модуль `webp2png.py` выполняет конвертацию WebP в PNG.
Модуль использует сторонние библиотеки `PIL` (Pillow) для обработки изображений, `header` для определения версии.

## Функции

### `convert_images`

```python
def convert_images(webp_dir: Path, png_dir: Path) -> None:
    """ Convert all WebP images in the specified directory to PNG format.

    Args:
        webp_dir (Path): Directory containing the source WebP images.
        png_dir (Path): Directory to save the converted PNG images.

    Example:
        convert_images(
            gs.path.google_drive / 'emil' / 'raw_images_from_openai',
            gs.path.google_drive / 'emil' / 'converted_images'
        )
    """
```

**Назначение**: Конвертирует все WebP изображения в указанной директории в формат PNG.

**Параметры**:
- `webp_dir` (Path): Директория, содержащая исходные WebP изображения.
- `png_dir` (Path): Директория для сохранения сконвертированных PNG изображений.

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Вызывает исключения**:
- Отсутствуют обработанные исключения.

**Как работает функция**:
1. Функция `convert_images` принимает на вход две директории: `webp_dir` (директория с WebP изображениями) и `png_dir` (директория для сохранения PNG изображений).
2.  Получает список имен файлов WebP из директории `webp_dir` с помощью функции `get_filenames`.
3.  Перебирает все файлы WebP в списке `webp_files`.
4.  Для каждого файла WebP формирует путь к PNG файлу, используя имя WebP файла без расширения и добавляя расширение ".png".
5.  Формирует полные пути к WebP и PNG файлам.
6.  Вызывает функцию `webp2png` для конвертации WebP в PNG.
7.  Выводит результат конвертации.

**ASCII flowchart**:

```
    Получение списка WebP файлов из webp_dir
    |
    Перебор файлов WebP
    |
    Создание пути к PNG файлу
    |
    Вызов webp2png для конвертации
    |
    Вывод результата конвертации
```

**Примеры**:

```python
from pathlib import Path
from src import gs
# from src.utils.convertors.webp2png import webp2png # Предполагается, что функция webp2png определена в другом месте

# Пример использования с указанием путей к директориям WebP и PNG
webp_dir = gs.path.google_drive / 'emil' / 'raw_images_from_openai'
png_dir = gs.path.google_drive / 'emil' / 'converted_images'
convert_images(webp_dir, png_dir)