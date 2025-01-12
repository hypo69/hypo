# Модуль `src.utils.convertors.png`

## Обзор

Модуль `src.utils.convertors.png` предназначен для генерации PNG изображений из текста. Он читает текст из файла или списка строк, создает PNG изображения для каждой строки и сохраняет их в указанную директорию. Модуль предоставляет настраиваемые параметры для внешнего вида изображений, такие как размер холста, шрифт, цвет текста и фона, а также уровень логирования.

## Содержание

1.  [Классы](#Классы)
    - [`TextToImageGenerator`](#TextToImageGenerator)
2.  [Функции](#Функции)
    - [`webp2png`](#webp2png)

## Классы

### `TextToImageGenerator`

**Описание**:
Класс для генерации PNG изображений из текста.

**Методы**:
- `__init__`: Инициализирует класс `TextToImageGenerator` с настройками по умолчанию.
- `generate_images`: Генерирует PNG изображения из предоставленных текстовых строк.
- `generate_png`: Создает PNG изображение с заданным текстом, шрифтом и цветами.
- `center_text_position`: Вычисляет позицию для центрирования текста на холсте.
- `overlay_images`: Накладывает одно PNG изображение на другое в указанной позиции.

#### `__init__`

**Описание**:
Инициализирует класс `TextToImageGenerator` с настройками по умолчанию.

**Параметры**:
- Нет

**Возвращает**:
- Нет

#### `generate_images`

**Описание**:
Генерирует PNG изображения из предоставленных текстовых строк.

**Параметры**:
- `lines` (List[str]): Список строк, из которых будут сгенерированы изображения.
- `output_dir` (str | Path, optional): Директория для сохранения выходных изображений. По умолчанию "./output".
- `font` (str | ImageFont.ImageFont, optional): Шрифт, используемый для текста. По умолчанию "sans-serif".
- `canvas_size` (Tuple[int, int], optional): Размер холста в пикселях. По умолчанию (1024, 1024).
- `padding` (float, optional): Процент размера холста, используемый в качестве пустой границы. По умолчанию 0.10.
- `background_color` (str, optional): Цвет фона для изображений. По умолчанию "white".
- `text_color` (str, optional): Цвет текста. По умолчанию "black".
- `log_level` (int | str | bool, optional): Уровень детализации логирования. По умолчанию "WARNING".
- `clobber` (bool, optional): Если True, то перезаписывает существующие файлы. По умолчанию False.

**Возвращает**:
- `List[Path]`: Список путей к сгенерированным PNG изображениям.

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

**Описание**:
Создает PNG изображение с заданным текстом, шрифтом и цветами.

**Параметры**:
- `text` (str): Текст, который будет отображен на изображении.
- `canvas_size` (Tuple[int, int]): Размер холста в пикселях.
- `padding` (float): Процент отступа, используемый в качестве границы.
- `background_color` (str): Цвет фона изображения.
- `text_color` (str): Цвет текста.
- `font` (str | ImageFont.ImageFont): Шрифт для текста.

**Возвращает**:
- `Image`: Сгенерированное PNG изображение.

#### `center_text_position`

**Описание**:
Вычисляет позицию для центрирования текста на холсте.

**Параметры**:
- `draw` (ImageDraw.Draw): Экземпляр `ImageDraw` для рисования.
- `text` (str): Текст, который нужно центрировать.
- `font` (ImageFont.ImageFont): Шрифт, используемый для текста.
- `canvas_size` (Tuple[int, int]): Размер холста в пикселях.

**Возвращает**:
- `Tuple[int, int]`: Координаты для центрирования текста.

#### `overlay_images`

**Описание**:
Накладывает одно PNG изображение поверх другого в указанной позиции.

**Параметры**:
- `background_path` (str | Path): Путь к фоновому PNG изображению.
- `overlay_path` (str | Path): Путь к PNG изображению наложения.
- `position` (tuple[int, int], optional): (x, y) координаты, где будет размещено наложение. По умолчанию (0, 0).
- `alpha` (float, optional): Уровень прозрачности изображения наложения (0.0 - 1.0). По умолчанию 1.0.

**Возвращает**:
- `Image`: Результирующее изображение с наложением.

**Пример**:
```python
    >>> result_image = overlay_images("background.png", "overlay.png", position=(50, 50), alpha=0.8)
    >>> result_image.save("result.png")
```

## Функции

### `webp2png`

**Описание**:
Конвертирует изображение в формате WEBP в формат PNG.

**Параметры**:
- `webp_path` (str): Путь к исходному файлу WEBP.
- `png_path` (str): Путь для сохранения конвертированного PNG файла.

**Возвращает**:
- `bool`: True, если конвертация прошла успешно.

**Пример**:
```python
    webp2png('image.webp', 'image.png')
```