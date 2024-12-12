# Анализ кода модуля `png.py`

**Качество кода: 6/10**

-   **Плюсы:**
    *   Код разбит на классы и функции, что обеспечивает модульность и читаемость.
    *   Используются типы для параметров функций и возвращаемых значений, что повышает надежность кода.
    *   Есть docstring для классов и функций, хотя и требует доработки.
    *   Реализована логика для генерации изображений из текста, центрирования текста, наложения изображений и конвертации webp в png.
    *   Используется `Pathlib` для работы с путями, что делает код более кроссплатформенным.

-   **Минусы:**
    *   Не используется `j_loads` или `j_loads_ns` для чтения файлов.
    *   Отсутствуют некоторые импорты.
    *   Docstring в формате reStructuredText (RST) требуется доработка.
    *   Не используется `logger.error` для обработки ошибок.
    *   Присутствует лишний `print` в функции `webp2png`.
    *   Используется устаревший способ определения размера текста, что может вызвать проблемы с некоторыми шрифтами.
    *   Не реализована полная настройка шрифтов, например, выбор конкретного файла шрифта.
    *   Комментарии в коде не соответствуют формату RST.
    *   Имена переменных не всегда соответствуют конвенции (некоторые имена могли бы быть более описательными).

**Рекомендации по улучшению**

1.  **Импорты:** Добавить отсутствующие импорты, такие как `Any` из `typing` .
2.  **Документация:** Переписать docstring в формате reStructuredText (RST). Добавить подробное описание параметров и возвращаемых значений для каждой функции и метода.
3.  **Обработка ошибок:** Заменить `try-except` блоки в `generate_images` и `webp2png` на использование `logger.error` для логирования ошибок.
4.  **Логирование:**  Использовать `from src.logger.logger import logger` для логирования ошибок.
5.  **Чтение файлов:** Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов, если это необходимо.
6.  **Шрифты:** Добавить возможность выбора файла шрифта, а не только имени шрифта.
7.  **Улучшение центрирования текста:** Применить метод `getbbox` для более точного определения размера текста.
8.  **Комментарии:** Переписать все комментарии в формате RST.
9.  **Именование переменных:** Пересмотреть имена переменных для улучшения читаемости кода.
10. **Удалить устаревшие коментарии:** Удалить коментарии, которые указывают на путь к файлу, так как это лишняя информация.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для конвертации текста в PNG изображения.
=========================================================================================

Этот модуль предоставляет класс :class:`TextToImageGenerator` для генерации PNG изображений из текста,
а также функцию :func:`webp2png` для конвертации WEBP изображений в PNG.

Пример использования
--------------------

Пример использования класса `TextToImageGenerator`:

.. code-block:: python

    generator = TextToImageGenerator()
    lines = ["Текст 1", "Текст 2", "Текст 3"]
    output_dir = "./output"
    images = await generator.generate_images(lines, output_dir=output_dir)
    print(images)

Пример использования функции `webp2png`:

.. code-block:: python

    webp2png('image.webp', 'image.png')
"""

from pathlib import Path
from typing import List, Tuple, Any
from PIL import Image, ImageDraw, ImageFont
from src.logger.logger import logger  # Logging


class TextToImageGenerator:
    """
    Класс для генерации PNG изображений из текста.

    :ivar default_output_dir: Путь к директории вывода по умолчанию.
    :vartype default_output_dir: Path
    :ivar default_canvas_size: Размер холста по умолчанию.
    :vartype default_canvas_size: Tuple[int, int]
    :ivar default_padding: Отступ по умолчанию.
    :vartype default_padding: float
    :ivar default_background: Цвет фона по умолчанию.
    :vartype default_background: str
    :ivar default_text_color: Цвет текста по умолчанию.
    :vartype default_text_color: str
    :ivar default_log_level: Уровень логирования по умолчанию.
    :vartype default_log_level: str
    
    :func `__init__`: Инициализирует класс TextToImageGenerator с настройками по умолчанию.
    :func `generate_images`: Генерирует PNG изображения из предоставленных текстовых строк.
    :func `generate_png`: Создает PNG изображение с заданным текстом, шрифтом и цветами.
    :func `center_text_position`: Вычисляет позицию для центрирования текста на холсте.
    :func `overlay_images`: Накладывает одно PNG изображение поверх другого в указанной позиции.
    :func `get_font_size`: Определяет размер шрифта на основе размера холста и отступа.
    :func `setup_logging`: Настраивает логирование на основе указанного уровня.
    """

    def __init__(self):
        """
        Инициализирует класс TextToImageGenerator с настройками по умолчанию.
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
        Генерирует PNG изображения из предоставленных текстовых строк.

        :param lines: Список строк, из которых будут сгенерированы изображения.
        :type lines: List[str]
        :param output_dir: Директория для сохранения выходных изображений.
        :type output_dir: str | Path, optional
        :param font: Шрифт для использования в тексте.
        :type font: str | ImageFont.ImageFont, optional
        :param canvas_size: Размер холста в пикселях.
        :type canvas_size: Tuple[int, int], optional
        :param padding: Процент размера холста, используемый в качестве пустой границы.
        :type padding: float, optional
        :param background_color: Цвет фона изображений.
        :type background_color: str, optional
        :param text_color: Цвет текста.
        :type text_color: str, optional
        :param log_level: Уровень детализации логирования.
        :type log_level: int | str | bool, optional
        :param clobber: Если True, перезаписывает существующие файлы.
        :type clobber: bool, optional
        :raises Exception: Если возникла ошибка при создании изображения.
        :return: Список путей к сгенерированным PNG изображениям.
        :rtype: List[Path]

        :Example:
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
            try:
                 img = self.generate_png(line, canvas_size, padding, background_color, text_color, font)
                 img.save(img_path)
                 generated_images.append(img_path)
            except Exception as e:
                logger.error(f"Error creating image for line: {line}, error: {e}")
                continue

        return generated_images

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
        Создает PNG изображение с заданным текстом, шрифтом и цветами.

        :param text: Текст для рендеринга на изображении.
        :type text: str
        :param canvas_size: Размер холста в пикселях.
        :type canvas_size: Tuple[int, int]
        :param padding: Процент отступа для использования в качестве границы.
        :type padding: float
        :param background_color: Цвет фона изображения.
        :type background_color: str
        :param text_color: Цвет текста.
        :type text_color: str
        :param font: Шрифт для использования в тексте.
        :type font: str | ImageFont.ImageFont
        :return: Сгенерированное PNG изображение.
        :rtype: Image
        """
        img = Image.new("RGB", canvas_size, background_color)
        draw = ImageDraw.Draw(img)
        font_size = self.get_font_size(canvas_size, padding)
        try:
            font = ImageFont.truetype(font, size=font_size)
        except OSError:
            font = ImageFont.load_default(size=font_size)

        text_position = self.center_text_position(draw, text, font, canvas_size)
        draw.text(text_position, text, fill=text_color, font=font)

        return img

    def center_text_position(
        self, draw: ImageDraw.Draw, text: str, font: ImageFont.ImageFont, canvas_size: Tuple[int, int]
    ) -> Tuple[int, int]:
        """
        Вычисляет позицию для центрирования текста на холсте.

        :param draw: Экземпляр ImageDraw.
        :type draw: ImageDraw.Draw
        :param text: Текст для рендеринга.
        :type text: str
        :param font: Шрифт, используемый для текста.
        :type font: ImageFont.ImageFont
        :param canvas_size: Размер холста в пикселях.
        :type canvas_size: Tuple[int, int]
        :return: Координаты для центрирования текста.
        :rtype: Tuple[int, int]
        """
        text_box = draw.textbbox((0, 0), text, font=font)
        text_width = text_box[2] - text_box[0]
        text_height = text_box[3] - text_box[1]
        return (canvas_size[0] - text_width) // 2, (canvas_size[1] - text_height) // 2

    def overlay_images(
        self,
        background_path: str | Path,
        overlay_path: str | Path,
        position: tuple[int, int] = (0, 0),
        alpha: float = 1.0,
    ) -> Image:
        """
        Накладывает одно PNG изображение поверх другого в указанной позиции.

        :param background_path: Путь к фоновому PNG изображению.
        :type background_path: str | Path
        :param overlay_path: Путь к PNG изображению для наложения.
        :type overlay_path: str | Path
        :param position: Координаты (x, y), где будет размещено наложение.
        :type position: tuple[int, int], optional
        :param alpha: Уровень прозрачности изображения для наложения (0.0 - 1.0).
        :type alpha: float, optional
        :return: Результирующее изображение с наложением.
        :rtype: Image

        :Example:
            >>> result_image = overlay_images("background.png", "overlay.png", position=(50, 50), alpha=0.8)
            >>> result_image.save("result.png")
        """
        # Открывает фоновое и накладываемое изображения
        try:
           background = Image.open(background_path).convert("RGBA")
           overlay = Image.open(overlay_path).convert("RGBA")
        except FileNotFoundError as e:
            logger.error(f'File not found: {e}')
            return None
        except Exception as e:
            logger.error(f'Error opening images: {e}')
            return None

        # Изменяет размер накладываемого изображения, чтобы соответствовать фоновому, если необходимо
        if overlay.size != background.size:
            overlay = overlay.resize(background.size, Image.LANCZOS)

        # Регулирует прозрачность накладываемого изображения
        overlay = overlay.copy()
        overlay.putalpha(int(alpha * 255))

        # Накладывает изображение на фон
        background.paste(overlay, position, overlay)

        return background

    def get_font_size(self, canvas_size: Tuple[int, int], padding: float) -> int:
        """
        Определяет размер шрифта на основе размера холста и отступа.

        :param canvas_size: Размер холста в пикселях.
        :type canvas_size: Tuple[int, int]
        :param padding: Процент отступа для использования в качестве границы.
        :type padding: float
        :return: Размер шрифта.
        :rtype: int
        """
        canvas_width, canvas_height = canvas_size
        available_width = canvas_width * (1 - 2 * padding)
        available_height = canvas_height * (1 - 2 * padding)
        return int(min(available_width, available_height) / 8)

    def setup_logging(self, level: int | str | bool = None):
       """
       Настраивает логирование на основе указанного уровня.

       :param level: Уровень логирования.
       :type level: int | str | bool, optional
       """
       if level:
            logger.setLevel(level)


def webp2png(webp_path: str, png_path: str) -> bool:
    """
    Конвертирует WEBP изображение в формат PNG.

    :param webp_path: Путь к входному файлу WEBP.
    :type webp_path: str
    :param png_path: Путь для сохранения конвертированного файла PNG.
    :type png_path: str
    :return: True, если конвертация успешна, иначе False.
    :rtype: bool

    :Example:
        webp2png('image.webp', 'image.png')
    """
    try:
        # Открывает webp изображение
        with Image.open(webp_path) as img:
            # Конвертирует в PNG и сохраняет
            img.save(png_path, 'PNG')
        return True
    except Exception as e:
        logger.error(f"Error during conversion: {e}")
        return False
```