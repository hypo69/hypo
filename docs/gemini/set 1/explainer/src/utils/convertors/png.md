# <input code>

```python
## \file hypotez/src/utils/convertors/png.py
# -*- coding: utf-8 -*-\n
#! venv/bin/python/python3.12

"""
.. module:: src.utils.convertors.png 
	:platform: Windows, Unix
	:synopsis: png convertors 
Module reads text from a file, generates PNG images for each line of text using Pillow,
and saves them to an output directory with customizable options for image appearance.
"""

from pathlib import Path
from typing import List, Tuple
from PIL import Image, ImageDraw, ImageFont
from src.logger.logger import logger  # Logging
```

```python
class TextToImageGenerator:
    """
    A class for generating PNG images from text lines.

    **Functions**:
    - `assign_path`: Determines the correct path for output PNG files, creating the directory if necessary.
    - `center_text_position`: Calculates the position to center text on the canvas.
    - `generate_png`: Creates a PNG image with the specified text, font, colors, etc.
    - `not_comment_or_blank`: Checks if a line is neither a comment nor blank.
    - `which_exist`: Checks which file names already exist in the directory.
    - `get_characters`: Extracts text lines from the input file or list, filtering out comments and blank lines.
    - `parse_size`: Parses a string into a `Size` object.
    - `get_max_text_size`: Computes the maximum text size based on the font and text lines.
    - `get_font`: Determines the font size based on canvas size and padding.
    - `setup_logging`: Configures logging based on the specified logging level.
    - `error`: Logs an error message and raises an exception.
    - `overlay_images`: Overlays one PNG image on top of another.
    """

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
        """
        # ... (rest of the generate_images function)
    
    # ... (rest of the class)
```

# <algorithm>

**Шаг 1:** Инициализация `TextToImageGenerator` с настройками по умолчанию.

**Пример:** Создание объекта `TextToImageGenerator` с предопределенными значениями для каталога вывода, размера холста, отступа и т.д.

**Шаг 2:**  Получение входных данных `lines` (список строк), параметров `output_dir`, `font`, `canvas_size`, `padding`, `background_color`, `text_color`, `log_level`, `clobber`.

**Пример:** Передача списка строк ("Строка 1", "Строка 2", "Строка 3") в качестве входных данных для создания изображений.

**Шаг 3:** Настройка логгирования на основе параметра `log_level`.

**Пример:** Установка уровня логгирования на "INFO".

**Шаг 4:** Обработка входных данных:
    * Если `canvas_size` или `padding` не заданы, используются значения по умолчанию.
    * Для каждой строки из списка `lines`:
        * Строится путь к файлу изображения.
        * Проверяется, существует ли файл с таким именем. Если он существует и `clobber` равен `False`, происходит пропускание строки.
        * Создаётся изображение `img` с помощью `generate_png`.
        * Изображение сохраняется в указанном каталоге.
        * Путь к сохранённому изображению добавляется в `generated_images`.

**Пример:** Если есть строка "Строка 1", будет создан файл "Строка 1.png".

**Шаг 5:** Возврат списка путей к сгенерированным изображениям.

**Пример:** Возвращается список `[Path("./output/Строка 1.png"), Path("./output/Строка 2.png")]`.


# <mermaid>

```mermaid
graph TD
    A[TextToImageGenerator] --> B{generate_images(lines, ...)};
    B --> C[setup_logging];
    B --> D{canvas_size, padding};
    D -- default --> E[if not canvas_size, if not padding];
    E --> F[use default values];
    F --> G[generated_images = []];
    B --> H[for line in lines];
    H --> I[img_path = output_directory / f"{line}.png"];
    I --> J{img_path.exists() and not clobber};
    J -- True --> K[logger.warning];
    J -- False --> L[img = generate_png(line, ...)];
    L --> M[img.save(img_path)];
    M --> N[generated_images.append(img_path)];
    N --> H;
    H --> O[return generated_images];
    K --> H;
    subgraph generate_png
        P[img = Image.new(...)]
        P --> Q[draw = ImageDraw.Draw(img)];
        Q --> R[font = ImageFont.truetype(...)];
        Q --> S[text_position = center_text_position(...)];
        S --> T[draw.text(text_position, ..., font=font)];
        T --> U[return img];
    end
    subgraph center_text_position
        V[text_width, text_height = draw.textsize(...)]
        V --> W{(canvas_size[0] - text_width) // 2, (canvas_size[1] - text_height) // 2}
        W --> Y[return coordinates];
    end
    
```

**Объяснение диаграммы:**

Диаграмма отображает поток данных в коде.  `generate_images` - главный метод, вызывающий `generate_png` и `center_text_position`.  `generate_png` отвечает за создание изображения, `center_text_position` — за вычисление позиции текста.  Зависимости от `PIL` и `pathlib` отображены.  `logger` из `src.logger.logger` используется для логгирования.


# <explanation>

**Импорты:**

- `from pathlib import Path`:  Импортирует класс `Path` для работы с путями к файлам в системе.  Используется для обработки путей к файлам изображений и каталогов вывода.
- `from typing import List, Tuple`: Импортирует типы данных `List` и `Tuple` для явного указания типов переменных, повышая читаемость и безопасность кода.
- `from PIL import Image, ImageDraw, ImageFont`: Импортирует необходимые классы из библиотеки Pillow для работы с изображениями: `Image` (для создания и обработки изображений), `ImageDraw` (для рисования текста и фигур на изображении), `ImageFont` (для работы с шрифтами).
- `from src.logger.logger import logger`: Импортирует модуль логгирования из файла `logger.py` внутри пакета `src`.  Это позволяет использовать логгирование для отслеживания операций и вывода сообщений об ошибках. Логгирование важно для отладки и ведения журнала.

**Классы:**

- `TextToImageGenerator`:  Представляет класс для генерации PNG изображений из текстовых строк.  Он имеет методы для обработки строк, расчета позиции текста, создания изображений и управления логгированием.  `__init__` инициализирует атрибуты класса с настройками по умолчанию.  `generate_images` — центральный метод, который обрабатывает ввод, создаёт изображения и сохраняет их.  `generate_png` отвечает за создание конкретного изображения.  `center_text_position` — вспомогательный метод для вычисления центрирования текста.  `overlay_images` позволяет накладывать изображение на изображение.

**Функции:**

- `generate_images`: Принимает список строк (`lines`), опциональные параметры для настройки выходного каталога, шрифта, размера холста, отступов, цвета фона и текста, уровня логгирования, и `clobber` для перезаписи существующих файлов.  Возвращает список путей к сгенерированным изображениям.

- `generate_png`: Создаёт изображение с заданным текстом, шрифтом, цветами и размерами.

- `center_text_position`: Вычисляет координаты для центрирования текста на холсте.

- `overlay_images`: Накладывает одно PNG изображение поверх другого в заданной позиции с определённой прозрачностью.

- `webp2png`: Преобразует WEBP изображение в PNG формат.

**Переменные:**

- `MODE`, `default_output_dir`, `default_canvas_size`, `default_padding`, `default_background`, `default_text_color`, `default_log_level`:  Константы и переменные-атрибуты, задающие значения по умолчанию для параметров генерации изображений.

**Возможные ошибки и улучшения:**

- Отсутствует проверка типов для параметров в `generate_images` и `generate_png` (например, проверка, что `canvas_size` — кортеж из двух целых чисел). Добавление проверок повысит надёжность кода.
- Отсутствие обработки исключений в `generate_images` для случая, когда `output_dir` не является валидным каталогом.
- Возвращаемое значение функции `webp2png` может быть улучшено, так как сейчас оно не всегда представляет информацию об успехе/неудачи преобразования. Нужно вернуть boolean.

**Взаимосвязь с другими частями проекта:**

Функция `generate_images` использует логгер `logger`, который, по всей видимости, определён в модуле `src.logger.logger`.  Это показывает зависимость от модуля логгирования.  Функция `webp2png` скорее всего, связана с другими преобразованиями изображений внутри проекта.  `PIL` (Pillow) — отдельная библиотека, а не часть проекта.