# Модуль конвертации WebP в PNG

## Обзор

Этот модуль предназначен для конвертации изображений из формата WebP в формат PNG. Он включает функцию `convert_images`, которая выполняет пакетную конвертацию файлов WebP, находящихся в указанной директории, и сохраняет их в формате PNG в другую директорию.

## Подробней

Модуль предназначен для автоматизации процесса конвертации изображений WebP в PNG. Это может быть полезно в случаях, когда необходимо обеспечить совместимость изображений с приложениями или платформами, не поддерживающими формат WebP. Функция `convert_images` использует функцию `webp2png` из модуля `src.utils.convertors.webp2png` для выполнения конвертации каждого отдельного файла.

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

**Описание**: Конвертирует все WebP изображения в указанной директории в формат PNG.

**Параметры**:
- `webp_dir` (Path): Директория, содержащая исходные WebP изображения.
- `png_dir` (Path): Директория для сохранения конвертированных PNG изображений.

**Возвращает**:
- `None`

**Примеры**:

```python
convert_images(
    gs.path.google_drive / 'emil' / 'raw_images_from_openai',
    gs.path.google_drive / 'emil' / 'converted_images'
)