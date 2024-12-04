# Модуль hypotez/src/utils/convertors/png.py

## Обзор

Модуль `png.py` предоставляет инструменты для генерации изображений PNG из текстовых строк, используя библиотеку Pillow. Он позволяет настраивать размер изображения, шрифт, цвета и другие параметры.  Также модуль включает функцию для конвертации WEBP в PNG.

## Классы

### `TextToImageGenerator`

**Описание**: Класс `TextToImageGenerator` отвечает за генерацию изображений PNG из текстовых данных. Он предоставляет методы для управления процессами создания изображений, включая настройку параметров и обработку ошибок.

**Методы**

#### `__init__(self)`

**Описание**: Инициализирует экземпляр класса с предопределенными значениями для параметров, таких как директория вывода, размер холста, отступ и цвета.

#### `generate_images(self, lines: List[str], output_dir: str | Path = None, ...)`

**Описание**: Генерирует список изображений PNG из переданного списка строк `lines`.

**Параметры**

- `lines` (List[str]): Список текстовых строк, из которых будут сгенерированы изображения.
- `output_dir` (str | Path, optional): Директория для сохранения выходных изображений. По умолчанию "./output".
- `font` (str | ImageFont.ImageFont, optional): Шрифт для текста. По умолчанию "sans-serif".
- `canvas_size` (Tuple[int, int], optional): Размер холста в пикселях. По умолчанию (1024, 1024).
- `padding` (float, optional): Процент размера холста, используемый как пустая граница. По умолчанию 0.10.
- `background_color` (str, optional): Цвет фона изображений. По умолчанию "white".
- `text_color` (str, optional): Цвет текста. По умолчанию "black".
- `log_level` (int | str | bool, optional): Уровень детализации логирования. По умолчанию "WARNING".
- `clobber` (bool, optional): Если True, перезаписывает существующие файлы. По умолчанию False.

**Возвращает**

- List[Path]: Список путей к сгенерированным изображениям PNG.

#### `generate_png(self, text: str, canvas_size: Tuple[int, int], padding: float, background_color: str, text_color: str, font: str | ImageFont.ImageFont) -> Image`

**Описание**: Создает изображение PNG с указанным текстом, шрифтом и цветами.

**Параметры**

- `text` (str): Текст для отображения на изображении.
- `canvas_size` (Tuple[int, int]): Размер холста в пикселях.
- `padding` (float): Отступ (процент) для создания границы.
- `background_color` (str): Цвет фона изображения.
- `text_color` (str): Цвет текста.
- `font` (str | ImageFont.ImageFont): Шрифт для текста.

**Возвращает**

- Image: Сгенерированное изображение PNG.

#### `center_text_position(self, draw: ImageDraw.Draw, text: str, font: ImageFont.ImageFont, canvas_size: Tuple[int, int]) -> Tuple[int, int]`

**Описание**: Вычисляет позицию для центрирования текста на холсте.

**Параметры**

- `draw` (ImageDraw.Draw): Экземпляр ImageDraw.
- `text` (str): Текст для центрирования.
- `font` (ImageFont.ImageFont): Используемый шрифт.
- `canvas_size` (Tuple[int, int]): Размер холста.

**Возвращает**

- Tuple[int, int]: Координаты для центрирования текста.


#### `overlay_images(self, background_path: str | Path, overlay_path: str | Path, position: tuple[int, int] = (0, 0), alpha: float = 1.0) -> Image`

**Описание**: Наложение одного изображения PNG поверх другого в заданной позиции.

**Параметры**:
    - `background_path`: Путь к фоновому изображению.
    - `overlay_path`: Путь к изображению наложения.
    - `position`: Координаты (x, y) для размещения изображения наложения.
    - `alpha`: Уровень прозрачности изображения наложения (от 0.0 до 1.0).

**Возвращает**: Результирующее изображение с наложенным изображением.


## Функции

### `webp2png(webp_path: str, png_path: str) -> bool`

**Описание**: Преобразует изображение WEBP в формат PNG.

**Параметры**:
    - `webp_path`: Путь к изображению WEBP.
    - `png_path`: Путь для сохранения преобразованного изображения PNG.

**Возвращает**:
    - `bool`: True, если преобразование прошло успешно, иначе `None`.