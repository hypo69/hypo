# Модуль для конвертации PNG изображений

## Обзор

Модуль `src.utils.convertors.png` предоставляет функциональность для работы с PNG изображениями, включая генерацию PNG изображений из текста и наложение одного изображения на другое. Он содержит класс `TextToImageGenerator`, который позволяет создавать PNG изображения из строк текста с различными настройками, такими как шрифт, размер холста, цвет фона и текста. Также, модуль содержит функцию `webp2png`, которая конвертирует изображения из формата WEBP в формат PNG.

## Подробней

Этот модуль предназначен для автоматической генерации изображений из текста, что может быть полезно для создания превью, водяных знаков или других визуальных элементов на основе текстовых данных. Класс `TextToImageGenerator` предоставляет гибкие настройки для создания изображений, а функция `webp2png` позволяет конвертировать изображения из формата WEBP в PNG.

## Классы

### `TextToImageGenerator`

**Описание**: Класс для генерации PNG изображений из текстовых строк.

**Как работает класс**:
Класс `TextToImageGenerator` инициализируется с настройками по умолчанию, такими как каталог вывода, размер холста, отступы, цвета фона и текста, а также уровень логирования. Он предоставляет методы для генерации изображений из текста, центрирования текста на холсте и наложения одного изображения на другое.

**Методы**:
- `__init__`: Инициализирует класс `TextToImageGenerator` с настройками по умолчанию.
- `generate_images`: Генерирует PNG изображения из предоставленных текстовых строк.
- `generate_png`: Создает PNG изображение с указанным текстом, шрифтом и цветами.
- `center_text_position`: Вычисляет позицию для центрирования текста на холсте.
- `overlay_images`: Накладывает одно PNG изображение на другое в указанной позиции.

**Параметры**:
- `default_output_dir` (Path): Путь к каталогу вывода по умолчанию (`./output`).
- `default_canvas_size` (Tuple[int, int]): Размер холста по умолчанию (1024x1024).
- `default_padding` (float): Отступ по умолчанию (0.10).
- `default_background` (str): Цвет фона по умолчанию ("white").
- `default_text_color` (str): Цвет текста по умолчанию ("black").
- `default_log_level` (str): Уровень логирования по умолчанию ("WARNING").

### `__init__`

```python
def __init__(self):
    """
    Initializes the TextToImageGenerator class with default settings.
    """
    self.default_output_dir = Path("./output")
    self.default_canvas_size = (1024, 1024)
    self.default_padding = 0.10
    self.default_background = "white"
    self.default_text_color = "black"
    self.default_log_level = "WARNING"
```

**Как работает функция**:
Функция инициализирует экземпляр класса `TextToImageGenerator` с настройками по умолчанию. Она устанавливает значения для каталога вывода, размера холста, отступов, цветов фона и текста, а также уровня логирования.

**Параметры**:
- Нет параметров.

**Возвращает**:
- Нет возвращаемого значения.

### `generate_images`

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
    output_directory = Path(output_dir) if output_dir else self.default_output_dir
    self.setup_logging(level=log_level)

    if not canvas_size:
        canvas_size = self.default_canvas_size

    if not padding:
        padding = self.default_padding

    generated_images = []
    for line in lines:
        img_path = output_directory / f"{line}.png"
        if img_path.exists() and not clobber:
            logger.warning(f"File {img_path} already exists. Skipping...")
            continue
        img = self.generate_png(line, canvas_size, padding, background_color, text_color, font)
        img.save(img_path)
        generated_images.append(img_path)

    return generated_images
```

**Как работает функция**:
Функция `generate_images` принимает список текстовых строк и генерирует PNG изображения для каждой строки. Она создает каталог вывода, если он не существует, и устанавливает уровень логирования. Для каждой строки текста она создает PNG изображение с использованием метода `generate_png` и сохраняет его в указанном каталоге вывода.

**Параметры**:
- `lines` (List[str]): Список строк для генерации изображений.
- `output_dir` (str | Path, optional): Каталог для сохранения выходных изображений. По умолчанию "./output".
- `font` (str | ImageFont.ImageFont, optional): Шрифт для использования в тексте. По умолчанию "sans-serif".
- `canvas_size` (Tuple[int, int], optional): Размер холста в пикселях. По умолчанию (1024, 1024).
- `padding` (float, optional): Процент от размера холста для использования в качестве пустой границы. По умолчанию 0.10.
- `background_color` (str, optional): Цвет фона для изображений. По умолчанию "white".
- `text_color` (str, optional): Цвет текста. По умолчанию "black".
- `log_level` (int | str | bool, optional): Уровень детализации логирования. По умолчанию "WARNING".
- `clobber` (bool, optional): Если `True`, перезаписывает существующие файлы. По умолчанию `False`.

**Возвращает**:
- `List[Path]`: Список путей к сгенерированным PNG изображениям.

### `generate_png`

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
    img = Image.new("RGB", canvas_size, background_color)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font, size=self.get_font_size(canvas_size, padding))

    text_position = self.center_text_position(draw, text, font, canvas_size)
    draw.text(text_position, text, fill=text_color, font=font)

    return img
```

**Как работает функция**:
Функция `generate_png` создает PNG изображение с указанным текстом, шрифтом и цветами. Она создает новое изображение с указанным размером холста и цветом фона, а затем рисует текст на изображении с использованием указанного шрифта и цвета текста.

**Параметры**:
- `text` (str): Текст для отображения на изображении.
- `canvas_size` (Tuple[int, int]): Размер холста в пикселях.
- `padding` (float): Процент отступа для использования в качестве границы.
- `background_color` (str): Цвет фона изображения.
- `text_color` (str): Цвет текста.
- `font` (str | ImageFont.ImageFont): Шрифт для использования в тексте.

**Возвращает**:
- `Image`: Сгенерированное PNG изображение.

### `center_text_position`

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
    text_width, text_height = draw.textsize(text, font=font)
    return (canvas_size[0] - text_width) // 2, (canvas_size[1] - text_height) // 2
```

**Как работает функция**:
Функция `center_text_position` вычисляет позицию для центрирования текста на холсте. Она измеряет ширину и высоту текста с использованием указанного шрифта, а затем вычисляет координаты для центрирования текста на холсте.

**Параметры**:
- `draw` (ImageDraw.Draw): Экземпляр `ImageDraw`.
- `text` (str): Текст для отображения.
- `font` (ImageFont.ImageFont): Шрифт для использования в тексте.
- `canvas_size` (Tuple[int, int]): Размер холста в пикселях.

**Возвращает**:
- `Tuple[int, int]`: Координаты для центрирования текста.

### `overlay_images`

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
    # Open the background and overlay images
    background = Image.open(background_path).convert("RGBA")
    overlay = Image.open(overlay_path).convert("RGBA")

    # Resize overlay to fit the background if needed
    if overlay.size != background.size:
        overlay = overlay.resize(background.size, Image.ANTIALIAS)

    # Adjust transparency of overlay
    overlay = overlay.copy()
    overlay.putalpha(int(alpha * 255))

    # Paste overlay onto background
    background.paste(overlay, position, overlay)

    return background
```

**Как работает функция**:
Функция `overlay_images` накладывает одно PNG изображение на другое в указанной позиции. Она открывает фоновое и накладываемое изображения, изменяет размер накладываемого изображения, чтобы соответствовать размеру фонового изображения, регулирует прозрачность накладываемого изображения и вставляет накладываемое изображение на фоновое изображение.

**Параметры**:
- `background_path` (str | Path): Путь к фоновому PNG изображению.
- `overlay_path` (str | Path): Путь к накладываемому PNG изображению.
- `position` (tuple[int, int], optional): Координаты (x, y), где будет размещено накладываемое изображение. По умолчанию (0, 0).
- `alpha` (float, optional): Уровень прозрачности накладываемого изображения (0.0 - 1.0). По умолчанию 1.0.

**Возвращает**:
- `Image`: Результирующее изображение с наложением.

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
    try:
        # Open the webp image
        with Image.open(webp_path) as img:
            # Convert to PNG and save
            img.save(png_path, 'PNG')
        return True
    except Exception as e:
        print(f"Error during conversion: {e}")
        return
```

**Как работает функция**:
Функция `webp2png` конвертирует изображение из формата WEBP в формат PNG. Она открывает WEBP изображение, конвертирует его в формат PNG и сохраняет его по указанному пути.

**Параметры**:
- `webp_path` (str): Путь к входному WEBP файлу.
- `png_path` (str): Путь для сохранения сконвертированного PNG файла.

**Возвращает**:
- `bool`: `True`, если конвертация прошла успешно, иначе `None`.

**Вызывает исключения**:
- `Exception`: Выводит сообщение об ошибке, если происходит ошибка во время конвертации.