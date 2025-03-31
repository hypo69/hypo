# Модуль `webp2png.py`

## Обзор

Модуль предназначен для конвертации изображений из формата WebP в формат PNG. Он включает функцию для пакетной конвертации всех WebP-файлов в указанной директории и сохранения результатов в другую директорию.

## Подробней

Этот модуль предоставляет функциональность для преобразования изображений WebP в PNG. Он использует функцию `webp2png` из модуля `src.utils.convertors.webp2png` для фактического преобразования каждого файла. Модуль полезен, когда требуется преобразовать большое количество изображений WebP в формат PNG, например, для совместимости с приложениями или платформами, которые не поддерживают WebP.

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

**Как работает функция**:
Функция `convert_images` принимает путь к директории с WebP-изображениями (`webp_dir`) и путь к директории, куда будут сохранены сконвертированные PNG-изображения (`png_dir`). Сначала она получает список всех WebP-файлов в указанной директории с помощью функции `get_filenames`. Затем, для каждого WebP-файла, она формирует путь к соответствующему PNG-файлу, используя имя WebP-файла без расширения. После этого вызывается функция `webp2png` для конвертации WebP-изображения в PNG, и результат конвертации выводится на экран.

**Параметры**:
- `webp_dir` (Path): Путь к директории, содержащей исходные WebP-изображения.
- `png_dir` (Path): Путь к директории, в которой будут сохранены сконвертированные PNG-изображения.

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Примеры**:

```python
convert_images(
    gs.path.google_drive / 'emil' / 'raw_images_from_openai',
    gs.path.google_drive / 'emil' / 'converted_images'
)
```
```python
convert_images(
    gs.path.google_drive / 'kazarinov' / 'raw_images_from_openai',
    gs.path.google_drive / 'kazarinov' / 'converted_images'
)