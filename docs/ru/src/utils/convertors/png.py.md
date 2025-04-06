# Модуль для преобразования текста в PNG изображения
## Обзор

Модуль `png.py` предназначен для генерации PNG изображений на основе текстовых строк. Он содержит класс `TextToImageGenerator`, который позволяет создавать изображения с настраиваемыми параметрами, такими как шрифт, размер холста, цвет фона и текста. Модуль также включает функцию `webp2png` для конвертации изображений из формата WEBP в формат PNG.

## Подробней

Этот модуль предоставляет инструменты для автоматической генерации изображений из текста, что может быть полезно для создания превью, водяных знаков или других визуальных элементов на основе текстовых данных. Класс `TextToImageGenerator` позволяет гибко настраивать внешний вид создаваемых изображений, а функция `webp2png` обеспечивает возможность конвертации изображений в формат PNG.

## Классы

### `TextToImageGenerator`

**Описание**: Класс `TextToImageGenerator` предназначен для генерации PNG изображений из текстовых строк. Он предоставляет методы для настройки параметров изображения, таких как размер холста, шрифт, цвет фона и текста, а также методы для вычисления положения текста на изображении.

**Принцип работы**:
1.  При инициализации класса устанавливаются значения по умолчанию для параметров генерации изображений, таких как размер выходной директории, размер холста, отступы, цвет фона и текста, а также уровень логирования.
2.  Метод `generate_images` принимает список текстовых строк и генерирует PNG изображения для каждой строки. Он проверяет наличие файла с таким же именем в выходной директории и, если файл существует и не разрешена перезапись, пропускает генерацию изображения для этой строки.
3.  Метод `generate_png` создает PNG изображение с заданным текстом, шрифтом и цветами. Он использует библиотеку PIL для создания изображения и добавления текста на него.
4.  Метод `center_text_position` вычисляет координаты для центрирования текста на холсте.
5.  Метод `overlay_images` накладывает одно PNG изображение на другое с заданным положением и прозрачностью.

**Аттрибуты**:

*   `default_output_dir` (Path): Путь к директории для сохранения сгенерированных изображений по умолчанию (`./output`).
*   `default_canvas_size` (Tuple[int, int]): Размер холста по умолчанию в пикселях (1024x1024).
*   `default_padding` (float): Отступ от края холста по умолчанию в процентах (0.10).
*   `default_background` (str): Цвет фона по умолчанию ("white").
*   `default_text_color` (str): Цвет текста по умолчанию ("black").
*   `default_log_level` (str): Уровень логирования по умолчанию ("WARNING").

**Методы**:

*   `__init__`: Инициализирует класс `TextToImageGenerator` со значениями по умолчанию.
*   `generate_images`: Генерирует PNG изображения из списка текстовых строк.
*   `generate_png`: Создает PNG изображение с заданным текстом, шрифтом и цветами.
*   `center_text_position`: Вычисляет координаты для центрирования текста на холсте.
*   `overlay_images`: Накладывает одно PNG изображение на другое с заданным положением и прозрачностью.

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

**Назначение**: Инициализирует класс `TextToImageGenerator` со значениями по умолчанию для параметров генерации изображений.

**Как работает функция**:

1.  Устанавливает значения по умолчанию для атрибутов класса, таких как путь к выходной директории, размер холста, отступы, цвет фона и текста, а также уровень логирования.

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
        [PosixPath(\'./output/Text 1.png\'), PosixPath(\'./output/Text 2.png\'), PosixPath(\'./output/Text 3.png\')]
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

**Назначение**: Генерирует PNG изображения из списка текстовых строк.

**Параметры**:

*   `lines` (List[str]): Список строк, содержащих текст для генерации изображений.
*   `output_dir` (str | Path, optional): Директория для сохранения сгенерированных изображений. По умолчанию "./output".
*   `font` (str | ImageFont.ImageFont, optional): Шрифт, используемый для текста. По умолчанию "sans-serif".
*   `canvas_size` (Tuple[int, int], optional): Размер холста в пикселях. По умолчанию (1024, 1024).
*   `padding` (float, optional): Процент от размера холста, используемый в качестве границы. По умолчанию 0.10.
*   `background_color` (str, optional): Цвет фона для изображений. По умолчанию "white".
*   `text_color` (str, optional): Цвет текста. По умолчанию "black".
*   `log_level` (int | str | bool, optional): Уровень детализации логирования. По умолчанию "WARNING".
*   `clobber` (bool, optional): Если `True`, перезаписывает существующие файлы. По умолчанию `False`.

**Возвращает**:

*   `List[Path]`: Список путей к сгенерированным PNG изображениям.

**Как работает функция**:

1.  Определяет выходную директорию для сохранения изображений. Если `output_dir` не указан, используется значение по умолчанию.
2.  Настраивает логирование на основе указанного уровня детализации.
3.  Если `canvas_size` не указан, используется размер холста по умолчанию.
4.  Если `padding` не указан, используется значение отступа по умолчанию.
5.  Итерируется по списку текстовых строк.
6.  Для каждой строки формирует путь к файлу изображения.
7.  Проверяет, существует ли файл с таким именем в выходной директории. Если файл существует и не разрешена перезапись (`clobber=False`), то выводится предупреждение в лог и происходит переход к следующей строке.
8.  Если файл не существует или разрешена перезапись, то вызывается метод `generate_png` для создания PNG изображения с заданными параметрами.
9.  Сохраняет сгенерированное изображение в файл.
10. Добавляет путь к сгенерированному изображению в список `generated_images`.
11. Возвращает список путей к сгенерированным изображениям.

**Примеры**:

```python
>>> generator = TextToImageGenerator()
>>> lines = ["Text 1", "Text 2", "Text 3"]
>>> output_dir = "./output"
>>> images = await generator.generate_images(lines, output_dir=output_dir)
>>> print(images)
[PosixPath('./output/Text 1.png'), PosixPath('./output/Text 2.png'), PosixPath('./output/Text 3.png')]
```

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

**Назначение**: Создает PNG изображение с заданным текстом, шрифтом и цветами.

**Параметры**:

*   `text` (str): Текст для отображения на изображении.
*   `canvas_size` (Tuple[int, int]): Размер холста в пикселях.
*   `padding` (float): Процент отступа, используемый в качестве границы.
*   `background_color` (str): Цвет фона изображения.
*   `text_color` (str): Цвет текста.
*   `font` (str | ImageFont.ImageFont): Шрифт, используемый для текста.

**Возвращает**:

*   `Image`: Сгенерированное PNG изображение.

**Как работает функция**:

1.  Создает новое RGB изображение с заданным размером холста и цветом фона.
2.  Создает объект `ImageDraw` для рисования на изображении.
3.  Загружает шрифт из файла и устанавливает размер шрифта на основе размера холста и отступа.
4.  Вычисляет координаты для центрирования текста на холсте с помощью метода `center_text_position`.
5.  Отрисовывает текст на изображении с заданным цветом и шрифтом.
6.  Возвращает сгенерированное изображение.

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

**Назначение**: Вычисляет координаты для центрирования текста на холсте.

**Параметры**:

*   `draw` (ImageDraw.Draw): Объект `ImageDraw` для рисования на изображении.
*   `text` (str): Текст для отображения на изображении.
*   `font` (ImageFont.ImageFont): Шрифт, используемый для текста.
*   `canvas_size` (Tuple[int, int]): Размер холста в пикселях.

**Возвращает**:

*   `Tuple[int, int]`: Кортеж координат (x, y) для центрирования текста.

**Как работает функция**:

1.  Измеряет ширину и высоту текста с использованием заданного шрифта.
2.  Вычисляет координаты для центрирования текста на холсте, вычитая ширину и высоту текста из ширины и высоты холста соответственно, а затем деля результат на 2.
3.  Возвращает вычисленные координаты.

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

**Назначение**: Накладывает одно PNG изображение на другое с заданным положением и прозрачностью.

**Параметры**:

*   `background_path` (str | Path): Путь к фоновому PNG изображению.
*   `overlay_path` (str | Path): Путь к накладываемому PNG изображению.
*   `position` (tuple[int, int], optional): Координаты (x, y), где будет размещено накладываемое изображение. По умолчанию (0, 0).
*   `alpha` (float, optional): Уровень прозрачности накладываемого изображения (0.0 - 1.0). По умолчанию 1.0.

**Возвращает**:

*   `Image`: Результирующее изображение с наложенным изображением.

**Как работает функция**:

1.  Открывает фоновое и накладываемое изображения, преобразуя их в формат RGBA.
2.  Если размеры накладываемого изображения не совпадают с размерами фонового изображения, изменяет размер накладываемого изображения, чтобы оно соответствовало размерам фонового изображения.
3.  Регулирует прозрачность накладываемого изображения на основе заданного уровня прозрачности (`alpha`).
4.  Вставляет накладываемое изображение на фоновое изображение в заданном положении.
5.  Возвращает результирующее изображение.

**Примеры**:

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
        webp2png(\'image.webp\', \'image.png\')
    """
    try:
        # Open the webp image
        with Image.open(webp_path) as img:
            # Convert to PNG and save
            img.save(png_path, \'PNG\')
        return True
    except Exception as e:
        print(f"Error during conversion: {e}")
        return
```

**Назначение**: Преобразует изображение из формата WEBP в формат PNG.

**Параметры**:

*   `webp_path` (str): Путь к входному файлу WEBP.
*   `png_path` (str): Путь для сохранения преобразованного PNG файла.

**Возвращает**:

*   `bool`: `True`, если преобразование прошло успешно, иначе `None`.

**Как работает функция**:

1.  Пытается открыть WEBP изображение по указанному пути.
2.  Если открытие прошло успешно, сохраняет изображение в формате PNG по указанному пути.
3.  Если в процессе возникают исключения, выводит сообщение об ошибке и возвращает `None`.

**Примеры**:

```python
webp2png('image.webp', 'image.png')