# Модуль `png`

## Обзор

Модуль `png` предоставляет инструменты для конвертации текста в PNG изображения, а также для наложения изображений друг на друга и конвертации изображений из формата WEBP в PNG. Он содержит класс `TextToImageGenerator`, который позволяет генерировать изображения из текста с различными настройками, такими как шрифт, размер холста, цвет фона и текста. Также в модуле присутствует функция `webp2png` для конвертации изображений из формата WEBP в PNG.

## Подробнее

Этот модуль предназначен для автоматической генерации изображений из текста, что может быть полезно для создания превью, водяных знаков или других визуальных элементов на основе текстовых данных. Класс `TextToImageGenerator` предоставляет гибкие настройки для кастомизации внешнего вида изображений. Функция `webp2png` позволяет конвертировать изображения из формата WEBP в PNG, что может быть необходимо для обеспечения совместимости с различными платформами и устройствами.

## Классы

### `TextToImageGenerator`

**Описание**: Класс для генерации PNG изображений из текстовых строк.

**Методы**:
- `__init__`: Инициализирует класс `TextToImageGenerator` настройками по умолчанию.
- `generate_images`: Генерирует PNG изображения из предоставленных текстовых строк.
- `generate_png`: Создает PNG изображение с указанным текстом, шрифтом и цветами.
- `center_text_position`: Вычисляет позицию для центрирования текста на холсте.
- `overlay_images`: Накладывает одно PNG изображение поверх другого в указанной позиции.

#### `__init__`

```python
    def __init__(self):
        """
        Initializes the TextToImageGenerator class with default settings.
        """
```

**Описание**: Инициализирует класс `TextToImageGenerator` значениями по умолчанию для выходного каталога, размера холста, отступов, цвета фона, цвета текста и уровня логирования.

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
            [PosixPath(\'./output/Text 1.png\'), PosixPath(\'./output/Text 2.png\'), PosixPath(\'./output/Text 3.png\')]
        """
```

**Описание**: Генерирует PNG изображения из предоставленных текстовых строк.

**Параметры**:
- `lines` (List[str]): Список строк, содержащих текст для генерации изображений.
- `output_dir` (str | Path, optional): Каталог для сохранения выходных изображений. По умолчанию "./output".
- `font` (str | ImageFont.ImageFont, optional): Шрифт, используемый для текста. По умолчанию "sans-serif".
- `canvas_size` (Tuple[int, int], optional): Размер холста в пикселях. По умолчанию (1024, 1024).
- `padding` (float, optional): Процент от размера холста, используемый в качестве пустой границы. По умолчанию 0.10.
- `background_color` (str, optional): Цвет фона для изображений. По умолчанию "white".
- `text_color` (str, optional): Цвет текста. По умолчанию "black".
- `log_level` (int | str | bool, optional): Уровень детализации логирования. По умолчанию "WARNING".
- `clobber` (bool, optional): Если True, перезаписывает существующие файлы. По умолчанию False.

**Возвращает**:
- `List[Path]`: Список путей к сгенерированным PNG изображениям.

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

**Описание**: Создает PNG изображение с указанным текстом, шрифтом и цветами.

**Параметры**:
- `text` (str): Текст для отображения на изображении.
- `canvas_size` (Tuple[int, int]): Размер холста в пикселях.
- `padding` (float): Процент отступа, используемый в качестве границы.
- `background_color` (str): Цвет фона изображения.
- `text_color` (str): Цвет текста.
- `font` (str | ImageFont.ImageFont): Шрифт, используемый для текста.

**Возвращает**:
- `Image`: Сгенерированное PNG изображение.

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

**Описание**: Вычисляет позицию для центрирования текста на холсте.

**Параметры**:
- `draw` (ImageDraw.Draw): Экземпляр `ImageDraw`.
- `text` (str): Текст для отображения.
- `font` (ImageFont.ImageFont): Шрифт, используемый для текста.
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

**Описание**: Накладывает одно PNG изображение поверх другого в указанной позиции.

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
        webp2png(\'image.webp\', \'image.png\')
    """
```

**Описание**: Преобразует изображение в формате WEBP в формат PNG.

**Параметры**:
- `webp_path` (str): Путь к входному WEBP файлу.
- `png_path` (str): Путь для сохранения преобразованного PNG файла.

**Возвращает**:
- `bool`: `True`, если преобразование прошло успешно, иначе `False`.

**Как работает функция**:
1. Открывает WEBP изображение по указанному пути.
2. Преобразует изображение в формат PNG.
3. Сохраняет преобразованное изображение по указанному пути.
4. В случае успеха возвращает `True`.
5. В случае ошибки выводит сообщение об ошибке и возвращает `None`.