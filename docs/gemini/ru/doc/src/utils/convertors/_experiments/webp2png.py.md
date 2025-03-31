# Модуль для конвертации изображений из WebP в PNG

## Обзор

Модуль предназначен для конвертации изображений из формата WebP в формат PNG. Он содержит функцию `convert_images`, которая выполняет конвертацию всех WebP-изображений из указанной директории в PNG-изображения и сохраняет их в другую директорию. В модуле используется функция `webp2png` для фактического преобразования формата изображений.

## Подробней

Этот модуль позволяет автоматизировать процесс конвертации изображений WebP в PNG, что может быть полезно, например, для обеспечения совместимости с приложениями или платформами, не поддерживающими формат WebP. Модуль использует функции `get_filenames` для получения списка файлов в указанной директории, а также `webp2png` для конвертации каждого файла.

## Функции

### `convert_images`

```python
def convert_images(webp_dir: Path, png_dir: Path) -> None:
    """
    Convert all WebP images in the specified directory to PNG format.

    Args:
        webp_dir (Path): Directory containing the source WebP images.
        png_dir (Path): Directory to save the converted PNG images.

    Example:
        convert_images(
            gs.path.google_drive / 'emil' / 'raw_images_from_openai',
            gs.path.google_drive / 'emil' / 'converted_images'
        )
    """
    ...
```

**Назначение**: Конвертирует все WebP-изображения в указанной директории в формат PNG.

**Как работает функция**:
1. Функция принимает на вход пути к директориям с WebP-изображениями (`webp_dir`) и для сохранения PNG-изображений (`png_dir`).
2. Использует функцию `get_filenames` для получения списка всех WebP-файлов в директории `webp_dir`.
3. Проходит по списку WebP-файлов и для каждого файла формирует путь к соответствующему PNG-файлу в директории `png_dir`.
4. Вызывает функцию `webp2png` для конвертации каждого WebP-файла в PNG-файл.
5. Печатает результат конвертации.

**Параметры**:
- `webp_dir` (Path): Директория, содержащая исходные WebP-изображения.
- `png_dir` (Path): Директория для сохранения конвертированных PNG-изображений.

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Примеры**:

```python
convert_images(
    gs.path.google_drive / 'emil' / 'raw_images_from_openai',
    gs.path.google_drive / 'emil' / 'converted_images'
)
```