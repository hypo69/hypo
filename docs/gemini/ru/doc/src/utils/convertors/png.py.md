# Модуль `png`

## Обзор

Модуль `png` предназначен для конвертации текста в изображения PNG. Он читает текст из файла или списка строк, генерирует PNG-изображения для каждой строки и сохраняет их в указанную директорию. Модуль предоставляет настройки для шрифта, размера холста, отступов, цветов и уровня логирования.

## Содержание

- [Классы](#классы)
    - [`TextToImageGenerator`](#texttoimagegenerator)
        - [`__init__`](#__init__)
        - [`generate_images`](#generate_images)
        - [`generate_png`](#generate_png)
        - [`center_text_position`](#center_text_position)
        - [`overlay_images`](#overlay_images)
- [Функции](#функции)
    - [`webp2png`](#webp2png)

## Классы

### `TextToImageGenerator`

**Описание**:
Класс для генерации PNG-изображений из текстовых строк.

**Методы**:
- `__init__`: Инициализирует класс `TextToImageGenerator` настройками по умолчанию.
- `generate_images`: Генерирует PNG-изображения из списка текстовых строк.
- `generate_png`: Создает PNG-изображение с заданным текстом, шрифтом и цветами.
- `center_text_position`: Вычисляет позицию для центрирования текста на холсте.
- `overlay_images`: Накладывает одно PNG-изображение поверх другого.

#### `__init__`
```python
def __init__(self) -> None:
    """
    Инициализирует класс TextToImageGenerator с настройками по умолчанию.
    """
```
**Описание**:
Инициализирует экземпляр класса `TextToImageGenerator` с настройками по умолчанию.

#### `generate_images`
```python
async def generate_images(
    self,
    lines: List[str],
    output_dir: str | Path = None,
    font: str | ImageFont.ImageFont = "sans-serif",
    canvas_size: Tuple[int, int] = None,
    padding: float = None,
    background_color: str = None,
    text_color: str = None,
    log_level: int | str | bool = None,
    clobber: bool = False,
) -> List[Path]:
    """
    Generates PNG images from the provided text lines.

    Args:
        lines (List[str]): A list of strings containing the text to generate images from.
        output_dir (str | Path, optional): Directory to save the output images. Defaults to "./output".
        font (str | ImageFont.ImageFont, optional): Font to use for the text. Defaults to "sans-serif".
        canvas_size (Tuple[int, int], optional): Size of the canvas in pixels. Defaults to (1024, 1024).
        padding (float, optional): Percentage of canvas size to use as a blank border. Defaults to 0.10.
        background_color (str, optional): Background color for the images. Defaults to "white".
        text_color (str, optional): Color of the text. Defaults to "black".
        log_level (int | str | bool, optional): Logging verbosity level. Defaults to "WARNING".
        clobber (bool, optional): If True, overwrites existing files. Defaults to False.

    Returns:
        List[Path]: A list of paths to the generated PNG images.

    Example:
        >>> generator = TextToImageGenerator()
        >>> lines = ["Text 1", "Text 2", "Text 3"]
        >>> output_dir = "./output"
        >>> images = await generator.generate_images(lines, output_dir=output_dir)
        >>> print(images)
        [PosixPath('./output/Text 1.png'), PosixPath('./output/Text 2.png'), PosixPath('./output/Text 3.png')]
    """
```
**Описание**:
Генерирует PNG-изображения из списка текстовых строк.

**Параметры**:
- `lines` (List[str]): Список строк с текстом для генерации изображений.
- `output_dir` (str | Path, optional): Директория для сохранения изображений. По умолчанию `./output`.
- `font` (str | ImageFont.ImageFont, optional): Шрифт текста. По умолчанию `"sans-serif"`.
- `canvas_size` (Tuple[int, int], optional): Размер холста в пикселях. По умолчанию `(1024, 1024)`.
- `padding` (float, optional): Процент от размера холста для отступов. По умолчанию `0.10`.
- `background_color` (str, optional): Цвет фона изображения. По умолчанию `"white"`.
- `text_color` (str, optional): Цвет текста. По умолчанию `"black"`.
- `log_level` (int | str | bool, optional): Уровень логирования. По умолчанию `"WARNING"`.
- `clobber` (bool, optional): Если `True`, перезаписывает существующие файлы. По умолчанию `False`.

**Возвращает**:
- `List[Path]`: Список путей к сгенерированным PNG-изображениям.

**Пример**:
```python
>>> generator = TextToImageGenerator()
>>> lines = ["Text 1", "Text 2", "Text 3"]
>>> output_dir = "./output"
>>> images = await generator.generate_images(lines, output_dir=output_dir)
>>> print(images)
[PosixPath('./output/Text 1.png'), PosixPath('./output/Text 2.png'), PosixPath('./output/Text 3.png')]
```

#### `generate_png`
```python
def generate_png(
    self,
    text: str,
    canvas_size: Tuple[int, int],
    padding: float,
    background_color: str,
    text_color: str,
    font: str | ImageFont.ImageFont,
) -> Image:
    """
    Creates a PNG image with the specified text, font, and colors.

    Args:
        text (str): Text to render on the image.
        canvas_size (Tuple[int, int]): Size of the canvas in pixels.
        padding (float): Padding percentage to use as a border.
        background_color (str): Background color of the image.
        text_color (str): Color of the text.
        font (str | ImageFont.ImageFont): Font to use for the text.

    Returns:
        Image: The generated PNG image.
    """
```
**Описание**:
Создает PNG-изображение с заданным текстом, шрифтом и цветами.

**Параметры**:
- `text` (str): Текст для рендеринга на изображении.
- `canvas_size` (Tuple[int, int]): Размер холста в пикселях.
- `padding` (float): Процент отступа от границ холста.
- `background_color` (str): Цвет фона изображения.
- `text_color` (str): Цвет текста.
- `font` (str | ImageFont.ImageFont): Шрифт для текста.

**Возвращает**:
- `Image`: Сгенерированное PNG-изображение.

#### `center_text_position`
```python
def center_text_position(
    self, draw: ImageDraw.Draw, text: str, font: ImageFont.ImageFont, canvas_size: Tuple[int, int]
) -> Tuple[int, int]:
    """
    Calculates the position to center the text on the canvas.

    Args:
        draw (ImageDraw.Draw): The ImageDraw instance.
        text (str): Text to be rendered.
        font (ImageFont.ImageFont): Font used for the text.
        canvas_size (Tuple[int, int]): Size of the canvas in pixels.

    Returns:
        Tuple[int, int]: Coordinates for centering the text.
    """
```
**Описание**:
Вычисляет позицию для центрирования текста на холсте.

**Параметры**:
- `draw` (ImageDraw.Draw): Экземпляр `ImageDraw`.
- `text` (str): Текст для рендеринга.
- `font` (ImageFont.ImageFont): Шрифт для текста.
- `canvas_size` (Tuple[int, int]): Размер холста в пикселях.

**Возвращает**:
- `Tuple[int, int]`: Координаты для центрирования текста.

#### `overlay_images`
```python
def overlay_images(
    self,
    background_path: str | Path,
    overlay_path: str | Path,
    position: tuple[int, int] = (0, 0),
    alpha: float = 1.0,
) -> Image:
    """Overlays one PNG image on top of another at a specified position.

    Args:
        background_path (str | Path): Path to the background PNG image.
        overlay_path (str | Path): Path to the overlay PNG image.
        position (tuple[int, int], optional): (x, y) coordinates where the overlay will be placed. Defaults to (0, 0).
        alpha (float, optional): Transparency level of the overlay image (0.0 - 1.0). Defaults to 1.0.

    Returns:
        Image: The resulting image with the overlay.

    Example:
        >>> result_image = overlay_images("background.png", "overlay.png", position=(50, 50), alpha=0.8)
        >>> result_image.save("result.png")
    """
```
**Описание**:
Накладывает одно PNG-изображение поверх другого в заданной позиции.

**Параметры**:
- `background_path` (str | Path): Путь к фоновому PNG-изображению.
- `overlay_path` (str | Path): Путь к накладываемому PNG-изображению.
- `position` (tuple[int, int], optional): Координаты (x, y) для размещения накладываемого изображения. По умолчанию `(0, 0)`.
- `alpha` (float, optional): Уровень прозрачности накладываемого изображения (0.0 - 1.0). По умолчанию `1.0`.

**Возвращает**:
- `Image`: Результирующее изображение с наложенным изображением.

**Пример**:
```python
>>> result_image = overlay_images("background.png", "overlay.png", position=(50, 50), alpha=0.8)
>>> result_image.save("result.png")
```

## Функции

### `webp2png`
```python
def webp2png(webp_path: str, png_path: str) -> bool:
    """
    Converts a WEBP image to PNG format.

    Args:
        webp_path (str): Path to the input WEBP file.
        png_path (str): Path to save the converted PNG file.

    Example:
        webp2png('image.webp', 'image.png')
    """
```
**Описание**:
Конвертирует изображение в формате WEBP в формат PNG.

**Параметры**:
- `webp_path` (str): Путь к входному файлу WEBP.
- `png_path` (str): Путь для сохранения конвертированного файла PNG.

**Возвращает**:
- `bool`: `True`, если конвертация прошла успешно, иначе возвращает `None`.

**Пример**:
```python
webp2png('image.webp', 'image.png')