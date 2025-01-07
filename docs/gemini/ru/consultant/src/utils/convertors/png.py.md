# Анализ кода модуля `png.py`

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован и разделен на классы и функции.
    - Присутствует документация в формате docstring для классов и методов.
    - Используются `Path` для работы с путями к файлам.
    - Логирование ошибок выполнено.
    - Код имеет примеры использования.
-  Минусы
    - Используется `print` для вывода ошибок, что не соответствует логированию.
    - Не используются `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Не все комментарии соответствуют reStructuredText (RST).
    - Есть избыточное использование `try-except`, `logger.error` необходимо использовать в блоке `except`.
    - Не везде соблюден стиль именования переменных, функций и классов.

**Рекомендации по улучшению**

1.  Заменить `print` на `logger.error` для логирования ошибок в функции `webp2png`.
2.  Добавить `from src.utils.jjson import j_loads, j_loads_ns` для возможного будущего использования.
3.  Переписать все комментарии в формате reStructuredText (RST), включая описание модуля, функций, методов и переменных.
4.  Убрать избыточные `try-except` блоки, используя `logger.error` для логирования ошибок.
5.  Привести имена переменных и функций к единому стилю (snake_case).
6.  Добавить более подробные описания к аргументам функций.
7.  Переписать docstring в более лаконичной форме.
8.  В функции `overlay_images` добавить проверку существования файлов перед их открытием.
9.  Использовать `Image.Resampling.LANCZOS` вместо `Image.ANTIALIAS` при изменении размера.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для генерации PNG изображений из текста.
==============================================================================

Этот модуль содержит класс :class:`TextToImageGenerator`, который используется для создания PNG
изображений из строк текста. Изображения могут быть настроены с помощью различных параметров,
таких как размер холста, цвет фона, цвет текста и шрифт.

Модуль также предоставляет функцию :func:`webp2png` для конвертации изображений WEBP в формат PNG.

Пример использования
--------------------

.. code-block:: python

    generator = TextToImageGenerator()
    lines = ["Text 1", "Text 2", "Text 3"]
    output_dir = "./output"
    images = await generator.generate_images(lines, output_dir=output_dir)
    print(images)
    # [PosixPath('./output/Text 1.png'), PosixPath('./output/Text 2.png'), PosixPath('./output/Text 3.png')]
"""
from pathlib import Path
from typing import List, Tuple
from PIL import Image, ImageDraw, ImageFont
from src.logger.logger import logger
from src.utils.jjson import j_loads, j_loads_ns  # Добавлен импорт




class TextToImageGenerator:
    """
    Класс для генерации PNG изображений из строк текста.

    :ivar default_output_dir: Путь к директории вывода по умолчанию.
    :vartype default_output_dir: pathlib.Path
    :ivar default_canvas_size: Размер холста по умолчанию (ширина, высота).
    :vartype default_canvas_size: tuple[int, int]
    :ivar default_padding: Отступ от края холста в процентах.
    :vartype default_padding: float
    :ivar default_background: Цвет фона по умолчанию.
    :vartype default_background: str
    :ivar default_text_color: Цвет текста по умолчанию.
    :vartype default_text_color: str
    :ivar default_log_level: Уровень логирования по умолчанию.
    :vartype default_log_level: str
    """

    def __init__(self):
        """
        Инициализация TextToImageGenerator с настройками по умолчанию.
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
        Генерирует PNG изображения из предоставленных строк текста.

        :param lines: Список строк для генерации изображений.
        :type lines: List[str]
        :param output_dir: Директория для сохранения изображений.
        :type output_dir: str | Path, optional
        :param font: Шрифт для текста.
        :type font: str | ImageFont.ImageFont, optional
        :param canvas_size: Размер холста (ширина, высота).
        :type canvas_size: Tuple[int, int], optional
        :param padding: Отступ от края холста в процентах.
        :type padding: float, optional
        :param background_color: Цвет фона.
        :type background_color: str, optional
        :param text_color: Цвет текста.
        :type text_color: str, optional
        :param log_level: Уровень логирования.
        :type log_level: int | str | bool, optional
        :param clobber: Перезаписывать существующие файлы.
        :type clobber: bool, optional
        :return: Список путей к сгенерированным PNG изображениям.
        :rtype: List[Path]

        Пример:
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

        :param text: Текст для отображения на изображении.
        :type text: str
        :param canvas_size: Размер холста (ширина, высота).
        :type canvas_size: Tuple[int, int]
        :param padding: Отступ от края холста в процентах.
        :type padding: float
        :param background_color: Цвет фона.
        :type background_color: str
        :param text_color: Цвет текста.
        :type text_color: str
        :param font: Шрифт для текста.
        :type font: str | ImageFont.ImageFont
        :return: Сгенерированное PNG изображение.
        :rtype: Image
        """
        img = Image.new("RGB", canvas_size, background_color)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(font, size=self.get_font_size(canvas_size, padding))

        text_position = self.center_text_position(draw, text, font, canvas_size)
        draw.text(text_position, text, fill=text_color, font=font)

        return img

    def center_text_position(
        self, draw: ImageDraw.Draw, text: str, font: ImageFont.ImageFont, canvas_size: Tuple[int, int]
    ) -> Tuple[int, int]:
        """
        Вычисляет позицию для центрирования текста на холсте.

        :param draw: Объект ImageDraw.
        :type draw: ImageDraw.Draw
        :param text: Текст для отображения.
        :type text: str
        :param font: Шрифт текста.
        :type font: ImageFont.ImageFont
        :param canvas_size: Размер холста (ширина, высота).
        :type canvas_size: Tuple[int, int]
        :return: Координаты для центрирования текста (x, y).
        :rtype: Tuple[int, int]
        """
        text_width, text_height = draw.textsize(text, font=font)
        return (canvas_size[0] - text_width) // 2, (canvas_size[1] - text_height) // 2

    def overlay_images(
        self,
        background_path: str | Path,
        overlay_path: str | Path,
        position: tuple[int, int] = (0, 0),
        alpha: float = 1.0,
    ) -> Image:
        """
        Накладывает одно PNG изображение на другое в заданной позиции.

        :param background_path: Путь к фоновому изображению.
        :type background_path: str | Path
        :param overlay_path: Путь к накладываемому изображению.
        :type overlay_path: str | Path
        :param position: Координаты (x, y) для наложения.
        :type position: tuple[int, int], optional
        :param alpha: Уровень прозрачности накладываемого изображения (0.0 - 1.0).
        :type alpha: float, optional
        :return: Изображение с наложенным слоем.
        :rtype: Image

        Пример:
            >>> result_image = overlay_images("background.png", "overlay.png", position=(50, 50), alpha=0.8)
            >>> result_image.save("result.png")
        """
        try:
            # проверка существования файлов
            if not Path(background_path).exists():
                logger.error(f"Фоновое изображение {background_path} не существует.")
                return None
            if not Path(overlay_path).exists():
                logger.error(f"Накладываемое изображение {overlay_path} не существует.")
                return None
            # открываем фоновое и накладываемое изображения
            background = Image.open(background_path).convert("RGBA")
            overlay = Image.open(overlay_path).convert("RGBA")

            # Изменяем размер накладываемого изображения, если необходимо
            if overlay.size != background.size:
                overlay = overlay.resize(background.size, Image.Resampling.LANCZOS)

            # Устанавливаем прозрачность накладываемого изображения
            overlay = overlay.copy()
            overlay.putalpha(int(alpha * 255))

            # Накладываем изображение
            background.paste(overlay, position, overlay)

            return background
        except Exception as ex:
             logger.error(f"Ошибка при наложении изображений: {ex}")
             return None



def webp2png(webp_path: str, png_path: str) -> bool:
    """
    Конвертирует изображение WEBP в формат PNG.

    :param webp_path: Путь к исходному WEBP файлу.
    :type webp_path: str
    :param png_path: Путь для сохранения PNG файла.
    :type png_path: str
    :return: True если конвертация прошла успешно, False в противном случае.
    :rtype: bool

    Пример:
        >>> webp2png('image.webp', 'image.png')
    """
    try:
        with Image.open(webp_path) as img:
            img.save(png_path, 'PNG')
        return True
    except Exception as e:
        logger.error(f"Ошибка при конвертации WEBP в PNG: {e}", exc_info=True)
        return False


    def get_font_size(self, canvas_size: Tuple[int, int], padding: float) -> int:
        """
        Определяет размер шрифта на основе размера холста и отступа.

        :param canvas_size: Размер холста (ширина, высота).
        :type canvas_size: Tuple[int, int]
        :param padding: Отступ от края холста в процентах.
        :type padding: float
        :return: Размер шрифта.
        :rtype: int
        """
        canvas_width, canvas_height = canvas_size
        padding_width = canvas_width * padding
        padding_height = canvas_height * padding
        available_width = canvas_width - 2 * padding_width
        available_height = canvas_height - 2 * padding_height
        return int(min(available_width, available_height) / 8) # TODO: fix magic number 8

    def setup_logging(self, level: int | str | bool = None):
        """
        Настраивает уровень логирования.

        :param level: Уровень логирования.
        :type level: int | str | bool, optional
        """
        if level:
            logger.setLevel(level)

```